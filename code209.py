class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.chap()

    def chap(self):
        print(self.name)
        print(self.age)

p=person(name='Ali',age=23)
