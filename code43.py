class Father:
    def chap(self):
        print("hello")

class Child(Father):
    def chap(self, name=None):
        if name:
            print("hello", name, sep="-")
        else:
            super().chap()

c = Child()
c.chap()         
c.chap("Ali")    
