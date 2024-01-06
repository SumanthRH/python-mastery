# make a new primitive type


class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"MutInt({self.value!r})"

    def __format__(self, fmt):
        return format(self.value, fmt)

    def __add__(self, other):
        if isinstance(other, MutInt):
            return self.value + other.value
        elif isinstance(other, int):
            return self.value + other
        else:
            return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
    
    __radd__ = __add__ # when operands are reversed