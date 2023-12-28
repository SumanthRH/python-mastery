import csv
from collections import namedtuple
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--datatype", type=str, choices=["tuple", "dict", "namedtuple", "class", "class_with_slots"], default="tuple")
# A class
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

NamedTupleRow = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

class EfficientRow:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def get_data(route, date, daytype, rides, data_type):
    if data_type == "tuple":
        return (route, date, daytype, rides)
    elif data_type == "dict":
        return {
            'route': route,
            'date': date,
            'daytype': daytype,
            'rides': rides,
        }
    elif data_type == "class":
        return Row(route, date, daytype, rides)
    elif data_type == "namedtuple":
        return NamedTupleRow(route, date, daytype, rides)
    elif data_type == "class_with_slots":
        return EfficientRow(route, date, daytype, rides)

def read_rides(filename, data_type):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = get_data(route, date, daytype, rides, data_type)
            records.append(record)
    return records

if __name__ == '__main__':
    args = parser.parse_args()
    data_type = args.datatype
    import tracemalloc
    tracemalloc.start()
    rows = read_rides('../Data/ctabus.csv', data_type=data_type)
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())