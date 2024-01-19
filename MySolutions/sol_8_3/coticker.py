from sol_8_1.structure import Structure
from .cofollow import consumer, follow
from sol_3_8.tableformat import create_formatter
import csv

class Ticker(Structure):
    name = String()
    price =Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

# This one is tricky. See solution for notes about it
@consumer
def to_csv(target):
    def producer():
        while True:
            yield line

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)

if __name__ == "__main__":
    ticker_fmter = ticker("text", ["name", "price", "change"])
    negative = negchange(ticker_fmter)
    records = create_ticker(negative)
    csv_producer = to_csv(records)

    lines = follow('../Data/stocklog.csv', csv_producer)



    
