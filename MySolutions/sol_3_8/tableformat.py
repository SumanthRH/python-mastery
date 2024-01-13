from sol_3_1.stock import read_portfolio
from abc import abstractmethod, ABC

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for obj in records:
        rowdata = [getattr(obj, attr) for attr in fields]
        formatter.row(rowdata)
        # print(values_fmt)

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    @abstractmethod
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


class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', "%d", "%0.2f"]

class UpperHeadersMixin:
    def headings(self, headers):
        headers = [s.upper() for s in headers]
        super().headings(headers)

class NewPortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass

def create_new_uh_class(cls):
    class PortfolioFormatter(UpperHeadersMixin, cls):
        pass
    return PortfolioFormatter()

def create_formatter(format, upper_headers):
    if format == "text":
        if upper_headers:
            return create_new_uh_class(TextTableFormatter)
        return TextTableFormatter()
    elif format == "csv":
        if upper_headers:
            return create_new_uh_class(CSVTableFormatter)
        return CSVTableFormatter()
    elif format == "html":
        if upper_headers:
            return create_new_uh_class(HTMLTableFormatter)
        return HTMLTableFormatter()
    else:
        raise ValueError(f"Unknown format {format}")


if __name__ == "__main__":
    portfolio = read_portfolio("../Data/portfolio.csv")
    formatter = create_formatter("text", upper_headers=True)
    print_table(portfolio, ["name","shares", "price"], formatter)