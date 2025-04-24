import copy

a=[[[1,2],[9,0]],[[3,4],[7,8]]]
b=a.copy()
print(b)
print(a==b)
print(a is b)

b[0][1][0]=10

print(a)
print(b)

c=copy.deepcopy(a)

c[0][1][0]=10

print(a)
print(c)
