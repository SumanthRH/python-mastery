from ..formatter import TableFormatter

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