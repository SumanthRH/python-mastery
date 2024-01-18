from typing import Any
import sys
import inspect 
from .validate import Validator, validated


def validate_attributes(cls):
    if not issubclass(cls, Structure):
        return cls
    validators = []
    types = []
    for attribute, value in vars(cls).items():
        if isinstance(value, Validator):
            validators.append(attribute)
            types.append(value.expected_type)
    cls._fields = tuple(validators)
    cls._types = tuple(types)
    # method wrapping
    for attribute, value in vars(cls).items():
        if callable(value):
            annotations = value.__annotations__
            if len(annotations):
                setattr(cls, attribute, validated(value))
    cls.create_init()
    return cls

class Structure:
    _fields = ()
    
    @classmethod
    def create_init(cls):
        argstr = ",".join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f"  self.{name} = {name}\n"
        loc = {}
        exec(code, loc)
        cls.__init__ = loc["__init__"]
    
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
    
    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        attrs = map(lambda x: getattr(self, x), self._fields)
        attr_reprs = ", ".join(map(repr, attrs))
        return f"{cls_name}({attr_reprs})"

    def __setattr__(self, name: str, value: Any) -> None:
        if (not name.startswith("_")) and name not in self._fields:
            raise AttributeError("No attribute %s" % name)
        super().__setattr__(name, value) # call to super is super important
    
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure, ),validators)
    return cls