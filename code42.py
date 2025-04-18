class a:
    def chap(self):
        print("hello")
    

class b:
    def chap(self,a):
        print(a)

a1=a()
b1=b()

a1.chap()
b1.chap(10)

