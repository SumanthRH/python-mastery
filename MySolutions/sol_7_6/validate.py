import inspect
from functools import wraps

class Validator:
    def __init__(self, name=None):
        self.name = name

    validators = {}
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls

    # set the name attr based on variable name assigned
    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
    

class Typed(Validator):
    expected_type = object
    # making this a class method helps us avoid work 
    # in creating instances
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f"Expected {cls.expected_type}")
        return super().check(value)

# class Integer(Typed):
#     expected_type = int

# class Float(Typed):
#     expected_type = float

# class String(Typed):
#     expected_type = str

_typed_classes = [
    ("Integer", int),
    ("Float", float),
    ("String", str),
    ("Complex", complex)
]

globals().update((name, type(name, (Typed,), {"expected_type": val})) 
                 for name, val in _typed_classes)


def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

def validated(func): 
    annotations = dict(func.__annotations__)
    # lovely signature binding
    sig = inspect.signature(func)
    annotations.pop("return", None) # remove the return type annotation
    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_sig = sig.bind(*args, **kwargs)
        errors = []
        for name, anno_type in annotations.items():
            val = bound_sig.arguments[name]
            try:
                type_check(val, anno_type)
            except TypeError as e:
                errors.append(f"{name} : {str(e)}")
        if len(errors) > 0:
            error_string = "\n".join(errors)
            raise TypeError(f"Bad Arguments\n{error_string}")
        result =func(*args, **kwargs)
        if sig.return_annotation is not inspect.Signature.empty:
            try:
                type_check(result, sig.return_annotation)
            except TypeError as e:
                raise TypeError(f"Bad return: {str(e)}")
        return result
    return wrapper

def enforce(**anno_kwargs):
    return_type = anno_kwargs.pop("return_", None)
    annotations = anno_kwargs
    def enforcer(func): 
        # lovely signature binding
        sig = inspect.signature(func)
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_sig = sig.bind(*args, **kwargs)
            errors = []
            for name, anno_type in annotations.items():
                val = bound_sig.arguments[name]
                try:
                    type_check(val, anno_type)
                except TypeError as e:
                    errors.append(f"{name} : {str(e)}")
            if len(errors) > 0:
                error_string = "\n".join(errors)
                raise TypeError(f"Bad Arguments\n{error_string}")
            result =func(*args, **kwargs)
            if return_type is not None:
                try:
                    type_check(result, return_type)
                except TypeError as e:
                    raise TypeError(f"Bad return: {str(e)}")
            return result
        return wrapper
    return enforcer

# class Stock:
#     name = String()
#     shares = PositiveInteger()
#     price = PositiveFloat()
    
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
    
#     @classmethod
#     def from_row(cls, row):
#         values = [func(val) for func, val in zip(cls._types, row)]
#         return cls(*values)
#     @property
#     def cost(self):
#         return self.shares * self.price
    
#     @enforce(nshares=PositiveInteger)
#     def sell(self, nshares: PositiveInteger):
#         self.shares = max(0, self.shares - nshares)
    
#     def __repr__(self) -> str:
#         return f"Stock(name='{self.name}', shares={self.shares}, price={self.price:.3f})"
    
#     def __eq__(self, other):
#         return isinstance(other, Stock) and (
#             (other.name, other.shares, other.price)==(self.name, self.shares, self.price)
#         )


def type_check(val, expected_type):
    if issubclass(expected_type, Typed):
        expected_type.check(val)
    elif not isinstance(val, expected_type):
        raise TypeError(f"Expected type {expected_type}")
    return