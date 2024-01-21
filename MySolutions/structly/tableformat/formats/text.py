from ..formatter import TableFormatter, ColumnFormatMixin, UpperHeadersMixin

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join('%10s' % h for h in headers))
        print(('-'*10 + " ")*len(headers))
    
    def row(self, rowdata):
        print(" ".join('%10s' % d for d in rowdata))

class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', "%d", "%0.2f"]

class NewPortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
    pass
