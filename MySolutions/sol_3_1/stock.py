import csv 

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    def sell(self, nshares):
        self.shares = max(0, self.shares - nshares)
    
def read_portfolio(filepath):
    portfolio = []
    with open(filepath) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        data = (dict(zip(headers, row)) for row in f_csv)
        for item in data:
            stock = Stock(item["name"], int(item["shares"]), float(item["price"]))
            portfolio.append(stock)
    return portfolio

def print_portfolio(portfolio):
    print('%10s %10s %10s' % ("name", "shares", "price"))
    print(f"{'-'*10} {'-'*10} {'-'*10}")
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == "__main__":
    portfolio = read_portfolio("../Data/portfolio.csv")
    print_portfolio(portfolio)