from typing import Any
import sys
import inspect 

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
    
    
    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        attrs = map(lambda x: getattr(self, x), self._fields)
        attr_reprs = ", ".join(map(repr, attrs))
        return f"{cls_name}({attr_reprs})"

    def __setattr__(self, name: str, value: Any) -> None:
        if (not name.startswith("_")) and name not in self._fields:
            raise AttributeError("No attribute %s" % name)
        self.__dict__[name] = value
        

class Date(Structure):
    _fields = ("year", "month", "day")
