lst=[1,2,3,4,5,6]

lst[0]=99

for items in lst:
    print(items)

for index in range(0,6):
    lst[index]=lst[index]**2

for items in lst:
    print(items)
