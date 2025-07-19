from collections import namedtuple

person=namedtuple('human',['age','name'])
p=person(age=10,name='ali')
print(p[0])
print(p[1])
