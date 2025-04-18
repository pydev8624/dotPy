from mod import *
# import mod

chap()
print(add(1,99))

class child(father):
    def __init__(self):
        super().__init__()
    
c=child()
c.age=10
c.name="Ali"
c.chap()

