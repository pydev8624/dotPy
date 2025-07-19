from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
person1 = Person(name='Ali', age=30)


print(person1)

person2 = person1._replace(age=31)


print(person2)
