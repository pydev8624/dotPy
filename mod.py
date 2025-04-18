def chap():
    print("hello")

def add(a,b):
    return a+b

class father:
    def __init__(self):
        self.name=None
        self.age=None
    def __change(self):
        self.name=""
    def chap(self):
        print(self.name,self.age)
    
    @staticmethod
    def adds(*num):
        return sum(num)

    @classmethod
    def clsadds(cls):
        # متد کلاس: به cls دسترسی دارد
        print(cls.adds(10,-5))

