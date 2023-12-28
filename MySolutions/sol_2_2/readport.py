import csv
from pprint import pprint
from collections import Counter
from sol_2_1.readrides import read_rides

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio

portfolio = read_portfolio('../Data/portfolio.csv')
pprint(portfolio)

list_comp = [s for s in portfolio if s['shares'] > 100]
pprint(list_comp)

total_cost = sum([s['shares']*s['price'] for s in portfolio])
pprint(total_cost)

print({ s["name"] for s in portfolio})

print("## Collections ##")
totals = Counter()
for s in portfolio:
    totals[s["name"]] += s["shares"]

print(totals)
print(totals.most_common(2))
# add two counters together
more = Counter()
more["IBM"] = 20
more["AAPL"] = 10
more["NEWSTCK"] = 10

print(totals + more)

print("## Exercise ## ")

# how many unique routes in chicago
rows = read_rides("../Data/ctabus.csv", "class_with_slots")
routes = set()
for row in rows:
    routes.add(row.route)
print("Number of bus routes in Chicago: ", len(routes))

my_date = "02/02/2011"
total_rides_my_date = sum([row.rides for row in rows if row.route == "22" and row.date == my_date])
print("Number of people who rode number 22 on February 2, 2011:", total_rides_my_date)

total_rides_per_route = Counter()
for row in rows:
    total_rides_per_route[row.route] += row.rides
print("Total rides per route: ", total_rides_per_route)

rides_in_2001 = Counter()
rides_in_2011 = Counter()
for row in rows:
    if row.date[-4:] == "2001":
        rides_in_2001[row.route] += row.rides
    if row.date[-4:] == "2011":
        rides_in_2011[row.route] += row.rides
increase_per_route = Counter()
for route in rides_in_2001:
    increase_per_route[route] = rides_in_2011[route] - rides_in_2001[route]

print("Five routes with the biggest increase: ", increase_per_route.most_common(5))