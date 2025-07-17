from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
p1 = Person(name='Ali', age=30)

print(p1.name)  
print(p1.age)   
