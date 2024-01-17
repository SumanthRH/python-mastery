from .logcall import logged
from .validate import Integer, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x+y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x**y


# print(pow(2, -1))