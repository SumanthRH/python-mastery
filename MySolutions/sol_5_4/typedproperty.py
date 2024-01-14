class MyTypedValidator:
    def __init__(self, expected_type, name=None):
        self.expected_type = expected_type
        self.name = "_" + name if name is not None else None
    
    # set the name attr based on variable name assigned
    def __set_name__(self, cls, name):
        self.name = "_" + name

    def check(self, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
    
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]
    

def typedproperty(expected_type, name=None):
    value = MyTypedValidator(expected_type, name=name)
    return value

def String():
    return typedproperty(str)

def Integer():
    return typedproperty(int)

def Float():
    return typedproperty(float)

class Stock:
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
