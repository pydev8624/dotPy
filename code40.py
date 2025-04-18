class father:
    def __init__(self):
        self._a=10

    def chap(self):
        print(self._a)

class child(father):
    def __init__(self):
        super().__init__()
    def chapn(self):
        # self._a=90                                                                                                                                                                      
        self.chap()

c=child()
c._a=0
c.chap()
c.chapn()
