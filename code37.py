class father:
    a=None
    def fun(self):
        print(self.a)

class child(father):
    b=None
    def fun1(self):
        print(self.a)
        print(self.b)
        self.fun()

c=child()
c.a=10
c.b=11
c.fun()
c.fun1()
