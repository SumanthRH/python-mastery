from sol_6_4.structure import Structure
import sys
from sol_7_1.validate import validated

class Stock(Structure):
    _fields = ("name", "shares", "price")
    def __init__(self, name, shares, price):
        self._init()
    
    @property
    def cost(self):
        return self.shares * self.price
    
    @validated
    def sell(self, nshares):
        self.shares -= nshares
    # sell = ValidatedFunction(sell)

Stock.create_init()