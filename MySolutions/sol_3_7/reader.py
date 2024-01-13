from abc import ABC, abstractmethod
import csv

class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types
    
    def make_record(self, headers, row):
        return {
            h: func(r) for h, func, r in 
            zip(headers, self.types, row)
        }
        
class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
    
def read_csv_as_instances(filepath, cls):
    parser = InstanceCSVParser(cls)
    return parser.parse(filepath)

def read_csv_as_dicts(filepath):
    parser = DictCSVParser([str, int, float])
    return parser.parse(filepath)

if __name__ == "__main__":
    parser = DictCSVParser([str, int, float])
    port = parser.parse("../Data/portfolio.csv")