class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Inside __new__ method")
        instance = super(MyClass, cls).__new__(cls)
        return instance

    def __init__(self):
        print("Inside __init__ method")
        

obj = MyClass()

