from abc import ABC, abstractmethod

__all__ = ["create_formatter", "print_table"]

class TableFormatter(ABC):
    _formats = {}
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()
    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()
    
    @classmethod
    def __init_subclass__(cls) -> None:
        name = cls.__module__.split(".")[-1]
        TableFormatter._formats[name] = cls

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        headers = [s.upper() for s in headers]
        super().headings(headers)

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for obj in records:
        rowdata = [getattr(obj, attr) for attr in fields]
        formatter.row(rowdata)
        # print(values_fmt)

def create_new_uh_class(cls):
    class PortfolioFormatter(UpperHeadersMixin, cls):
        pass
    return PortfolioFormatter()


def create_formatter(format, upper_headers=None, column_formats=None):
    if format not in TableFormatter._formats:
        __import__(f"{__package__}.formats.{format}")

    cls = TableFormatter._formats.get(format)
    if not cls:        
        raise ValueError(f"Unknown format {format}")

    if upper_headers:
        class cls(UpperHeadersMixin, cls):
            pass

    if column_formats:
        class cls(ColumnFormatMixin, cls):
            pass
    
    return cls()
