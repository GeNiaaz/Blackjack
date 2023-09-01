from io import StringIO
class StringBuilder:
    string = None
 
    def __init__(self):
        self.string = StringIO()
 
    def add(self, str):
        self.string.write(str)
 
    def __str__(self):
        return self.string.getvalue()