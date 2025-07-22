class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.chap()

    def chap(self):
        print(self.name)
        print(self.age)

class man(person):
    def __init__(self, name, age):
        super().__init__(name, age)

m=man(name='ali',age=35)
