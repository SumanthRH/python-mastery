from sol_3_1.stock import read_portfolio

def print_table(objs, attrs):
    header = " ".join(['%10s' % attr for attr in attrs])
    sep = " ".join(['-'*10 for attr in attrs])
    print(header)
    print(sep)
    for obj in objs:
        values = [getattr(obj, attr) for attr in attrs]
        values_fmt = " ".join(["%10s" % val for val in values])
        print(values_fmt)

if __name__ == "__main__":
    portfolio = read_portfolio("../Data/portfolio.csv")
    print_table(portfolio, ["name","shares", "price"])