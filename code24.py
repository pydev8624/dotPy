def fun(a=-1,b=-1,c=-1):
    a+=1
    b+=1
    c+=1
    return a,b,c

v1,v2,v3=fun(10,20,30)
print(v1,v2,v3)

v1,v2,v3=fun()
print(v1,v2,v3)


