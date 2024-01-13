from sol_3_1.stock import read_portfolio

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for obj in records:
        rowdata = [getattr(obj, attr) for attr in fields]
        formatter.row(rowdata)
        # print(values_fmt)

class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join('%10s' % h for h in headers))
        print(('-'*10 + " ")*len(headers))
    
    def row(self, rowdata):
        print(" ".join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))
    
    def row(self, rowdata):
        print(",".join('%s' % d for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        start = "<tr> "
        end = " </tr>"
        substr = " ".join(f"<th>{h}</th>" for h in headers)
        print(start + substr + end)
    
    def row(self, rowdata):
        start = "<tr> "
        end = " </tr>"
        substr = " ".join(f"<td>{d}</td>" for d in rowdata)
        print(start + substr + end)

def create_formatter(format):
    if format == "text":
        return TextTableFormatter()
    elif format == "csv":
        return CSVTableFormatter()
    elif format == "html":
        return HTMLTableFormatter()
    else:
        raise ValueError(f"Unknown format {format}")

if __name__ == "__main__":
    portfolio = read_portfolio("../Data/portfolio.csv")
    formatter = create_formatter("csv")
    print_table(portfolio, ["name","shares", "price"], formatter)