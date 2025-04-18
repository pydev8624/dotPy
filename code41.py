class father:
    def __init__(self):
        self.__a=None

    def __chap(self):
        print(self.__a)
    def chapf(self):
        self.__chap()

class child(father):
    def __init__(self):
        super().__init__()
    def chapn(self):
        self.__a=90                                                                                                                                                                      
        self.chap()

f=father()
f.__a=100
f.chapf()

c=child()
c.__a=0
c.__chap()
c.chapn()
