class Validator:
    def __init__(self, name=None):
        self.name = name
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

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

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

class Stock:
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares = max(0, self.shares - nshares)
    
    def __repr__(self) -> str:
        return f"Stock(name='{self.name}', shares={self.shares}, price={self.price:.3f})"
    
    def __eq__(self, other):
        return isinstance(other, Stock) and (
            (other.name, other.shares, other.price)==(self.name, self.shares, self.price)
        )
