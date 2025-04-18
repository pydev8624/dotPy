class father:
    def __init__(self):
        self.a=10
        
    def chap(self):
        print(self.a)

class child(father):
    def __init__(self):
        super().__init__()
    def chapn(self):
        self.a=90
        self.chap()

c=child()
c.chap()
c.chapn()
