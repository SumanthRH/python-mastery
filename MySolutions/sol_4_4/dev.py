class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def __setattr__(self, name, value):
        if name not in { 'name', 'shares', 'price' }:
            raise AttributeError('No attribute %s' % name)
        super().__setattr__(name, value)

class Readonly:
    def __init__(self, obj):
        self.__dict__['_obj'] = obj
    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute")
    def __getattr__(self, name):
        return getattr(self._obj, name)

class Spam:
    def a(self):
        print('Spam.a')
    def b(self):
        print('Spam.b')


class MySpam:
    def __init__(self):
        self._spam = Spam()
    def a(self):
        print('MySpam.a')
        self._spam.a()
    def c(self):
        print('MySpam.c')
    def __getattr__(self, name):
        return getattr(self._spam, name)