import csv 
from decimal import Decimal
from typing import Union

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
    
    def cost(self):
        return self.shares * self.price
    def sell(self, nshares):
        self.shares = max(0, self.shares - nshares)
    def __repr__(self) -> str:
        return f"Stock(name={self.name}, nshares={self.shares}, price={self.price:.3f})"
    
class DStock(Stock):
    types = (str, int, Decimal)

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
    portfolio = read_csv_as_instances("../Data/portfolio.csv", cls=DStock)
    print_portfolio(portfolio)