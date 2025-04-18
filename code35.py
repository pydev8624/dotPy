class human:
    name="Ali"
    def fun1(self):
        print(self.name)
    def fun2(self):
        self.fun1()

h=human()
h.fun2()
