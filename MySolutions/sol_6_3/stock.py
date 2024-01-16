from sol_6_3.structure import Structure
import sys

class Stock(Structure):
    _fields = ("name", "shares", "price")
    def __init__(self, name, shares, price):
        self._init()
    
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.set_fields()