class nobj:
    def __new__(cls):
        no=super().__new__(cls)
        return no

o=nobj
newo=o 
