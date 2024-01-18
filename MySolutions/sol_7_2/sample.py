from .logcall import logged
from .validate import Integer, enforce

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x+y

@enforce(x=Integer, y=Integer, return_=Integer)
def pow(x, y):
    return x**y


# print(pow(2, -1))