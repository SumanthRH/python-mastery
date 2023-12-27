import os

def portfolio_cost(filepath):
    with open(filepath, "r") as f:
        data = f.readlines()

    total_cost = 0
    for line in data:
        name, num_shares, price_per_share = line.strip("\n").split()
        try:
            num_shares = int(num_shares)
            price_per_share = float(price_per_share)
        except ValueError as e:
            print(Warning(f"Couldn't parse: {line}Reason: {e}"))
            continue
        cost = num_shares * price_per_share
        total_cost += cost 
    return total_cost

if __name__ == "__main__": 
    print(portfolio_cost("../Data/portfolio.dat"))