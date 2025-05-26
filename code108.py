i=int(input("number : "))
t=0
for item in [-2,-1,1,2,3]:
    try:
        t=i/item
    except Exception as error:
        print(error)
    else:
        print(t)
    
