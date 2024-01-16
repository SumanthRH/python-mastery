from typing import Any
import sys

class Structure:
    _fields = ()
    
    # staticmethod since we extract self from locals
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals # Gets the local variables of the caller
        self = locs.pop("self")
        for name, val in locs.items():
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
