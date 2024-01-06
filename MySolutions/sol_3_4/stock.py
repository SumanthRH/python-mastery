import csv 
from decimal import Decimal
from typing import Union

class Stock:
    _types = (str, int, float)
    __slots__ = ("name", "_shares", "_price")
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise ValueError(f"Expected a {self._types[0]}")
        if value < 0:
            raise ValueError("shares must be >=0")
        self._shares = value 
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise ValueError(f"Expected a {self._types[2]}")
        if value < 0:
            raise ValueError("price must be >=0")
        self._price = value 
    
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
        return f"Stock(name={self.name}, nshares={self.shares}, price={self.price:.3f})"
    
class DStock(Stock):
    _types = (str, int, Decimal)

def read_csv_as_instances(filepath, cls : Union[Stock, DStock]):
    portfolio = []
    with open(filepath) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        # data = (dict(zip(headers, row)) for row in f_csv)
        for row in f_csv:
            stock = cls.from_row(row)
            portfolio.append(stock)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ("name", "shares", "price"))
    print(f"{'-'*10} {'-'*10} {'-'*10}")
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == "__main__":
    portfolio = read_csv_as_instances("../Data/portfolio.csv", cls=Stock)
    print_portfolio(portfolio)