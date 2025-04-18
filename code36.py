class father:
    def __init__(self):
        self.name=None
        self.age=None

f=father()
print(f.name,f.age,sep="-")

class mother:
    def __init__(self,name,age):
        self.name=name
        self.age=age 

m=mother("Mom",30)
print(m.name,m.age,sep="-")
