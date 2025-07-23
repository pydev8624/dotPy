class SimpleNamedTuple:
    def __init__(self, typename, field_names):
        self.typename = typename  

    def __call__(self, name, age):
        typename = self.typename

        class PersonLike:
            def __new__(cls, name, age):
                obj = object.__new__(cls)
                obj.name = name
                obj.age = age
                return obj

        PersonLike.__name__ = typename
        return PersonLike(name, age)


Person = SimpleNamedTuple('Person', ['name', 'age'])
p = Person('Ali', 30)

print(p.name) 
print(p.age)   
