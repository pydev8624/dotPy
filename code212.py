class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "Object created"
    def __repr__(self):
        return "Object created version 0.1"
    
p=person(name='ali',age=33)
print(str(p))
print(repr(p))
print(p)
    
