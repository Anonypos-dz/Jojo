'''
Dear programmer,\n
My script is working SO DON'T FUCKING TOUCH IT.\n
Anonypos,
'''
class Jojo:
    """Programmed by Anonypos.\n
    Don't fucking touch my script it's working :)"""
    def __init__(self,title : str):
        self.space = "    "
        self.title = title
        self.body=f"""
<!DOCTYPE html>
<html>
    <head>
        <title>{self.title}</title>
        <!--Programmed by Anonypos(head)-->
    </head>
    <body>
        <!--Programmed by Anonypos(body)-->
    </body>
</html>
"""
    def body_add_element(self,name : str,content : str = None,attributes = None):
        """Add any html argument.
        ____________________________
        name:
            <{name}></{name}>
        content:
            <{name}>{content}</{name}>
        attributes:
            <{name} {attributes}></{name}>
        
        the finale element:
            <{name} {attributes}>{content}</{name}>
        ____________________________
        And that's it, IT'S FUCKING SIMPLE."""
        if name not in ["br","hr","img","input"]:
            if attributes != None:
                element  = f"<{name} {attributes}>{content}</{name}>\n{self.space*2}<!--Programmed by Anonypos(body)-->"
            else:
                element = f"<{name}>{content}</{name}>\n{self.space*2}<!--Programmed by Anonypos(body)-->" 
        else:
            if attributes != None:
                element = f"<{name} {attributes}>\n{self.space*2}<!--Programmed by Anonypos(body)-->"
            else:
                element = f"<{name}>\n{self.space*2}<!--Programmed by Anonypos(body)-->"
        self.body = self.body.replace("<!--Programmed by Anonypos(body)-->",element).strip()
        return self.body
    def head_add_element(self,name : str,content : str = None,attributes = None):
        if name not in ["meta","link"]:
            if attributes != None:
                element  = f"<{name} {attributes}>{content}</{name}>\n{self.space*2}<!--Programmed by Anonypos(head)-->"
            else:
                element = f"<{name}>{content}</{name}>\n{self.space*2}<!--Programmed by Anonypos(head)-->" 
        else:
            if attributes != None:
                element = f"<{name} {attributes}>\n{self.space*2}<!--Programmed by Anonypos(head)-->"
            else:
                element = f"<{name}>\n{self.space*2}<!--Programmed by Anonypos(head)-->"
        self.body = self.body.replace("<!--Programmed by Anonypos(head)-->",element).strip()
        return self.body
    def add_table(self,rows:list[list[str]],table_attributes : str= None):
        """To create the table rows you need to pass a list of lists.\n
        exemple:
            from jojo import Jojo as jj
            page = jj("Test")
            header_attributes = "id='header'"
            row_attributes = "id='row'"
            data_attributes = "id='data'"
            page.add_table(rows=[
            ["Header1","Data1",,header_attributes,data_attributes],
            ["Header2","Data2"] #You can write nothing for the attributes
            ],
            table_attributes="id='table_1'")
        """
        if table_attributes != None:
            element = f"<table {table_attributes}>\n{self.space*3}<!--Programmed by Anonypos(table)-->\n{self.space*2}</table>\n{self.space*2}<!--Programmed by Anonypos(body)-->"
            self.body = self.body.replace("<!--Programmed by Anonypos(body)-->",element).strip()
        else:
            element = f"<table>\n{self.space*3}<!--Programmed by Anonypos(table)-->\n{self.space*2}</table>\n{self.space*2}<!--Programmed by Anonypos(body)-->"
            self.body = self.body.replace("<!--Programmed by Anonypos(body)-->",element).strip()           
        for row in rows:
            if len(row) <=2:
                self.body = self.body.replace("<!--Programmed by Anonypos(table)-->",f"<tr><th>{row[0]}</th><td>{row[1]}</td></tr>\n{self.space*3}<!--Programmed by Anonypos(table)-->")
            else:
                if len(row) == 3:
                    self.body = self.body.replace("<!--Programmed by Anonypos(table)-->",f"<tr {row[2]}><th>{row[0]}</th><td>{row[1]}</td></tr>\n{self.space*3}<!--Programmed by Anonypos(table)-->")
                elif len(row) == 4:
                    self.body = self.body.replace("<!--Programmed by Anonypos(table)-->",f"<tr {row[2]}><th {row[3]}>{row[0]}</th><td>{row[1]}</td></tr>\n{self.space*3}<!--Programmed by Anonypos(table)-->")
                elif len(row) == 5:
                    self.body = self.body.replace("<!--Programmed by Anonypos(table)-->",f"<tr {row[2]}><th {row[3]}>{row[0]}</th><td {row[4]}>{row[1]}</td></tr>\n{self.space*3}<!--Programmed by Anonypos(table)-->")
    def get_page(self):
        return self.body
        