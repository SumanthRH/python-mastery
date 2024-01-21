from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))
    
    def row(self, rowdata):
        print(",".join('%s' % d for d in rowdata))