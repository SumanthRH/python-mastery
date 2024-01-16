from typing import Any


class Structure:
    _fields = ()
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")
        for name, val in zip(self._fields, args):
            setattr(self, name, val)
    
    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        attrs = map(lambda x: getattr(self, x), self._fields)
        attr_reprs = ",".join(map(repr, attrs))
        return f"{cls_name}({attr_reprs})"

    def __setattr__(self, name: str, value: Any) -> None:
        if (not name.startswith("_")) and name not in self._fields:
            raise AttributeError("No attribute %s" % name)
        self.__dict__[name] = value
        

class Date(Structure):
    _fields = ("year", "month", "day")
