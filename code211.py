class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "Object created"
    

p=person(name='ali',age=30)
print(p)
print(str(p))
