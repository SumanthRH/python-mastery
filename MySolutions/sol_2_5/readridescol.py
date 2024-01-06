from collections.abc import Sequence
import csv 
from sol_2_1.readrides import get_data

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []
    
    def __getitem__(self, idx):
        return {"route": self.routes[idx], 
                "date": self.dates[idx], 
                "daytype": self.daytypes[idx],
                "rides": self.numrides[idx]}

    def __len__(self):
        return len(self.routes)
    
    def append(self, d):
        self.routes.append(d["route"])
        self.dates.append(d["date"])
        self.daytypes.append(d["daytype"])
        self.numrides.append(d["rides"])

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = get_data(route, date, daytype, rides, "dict")
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_dicts('../Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())