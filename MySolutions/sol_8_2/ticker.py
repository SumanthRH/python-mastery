from sol_8_1.structure import Structure
from sol_3_8.tableformat import create_formatter, print_table
class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

if __name__ == '__main__':
    from sol_8_1.follow import follow
    import csv
    lines = follow('../Data/stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    formatter = create_formatter("text")
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ["name", "price", "change"], formatter)