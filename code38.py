class father:
    a=10
    def chap(self):
        print(self.a)

class child(father):
    pass

c=child()
c.a=90
c.chap()
