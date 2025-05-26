i=int(input("number : "))
for item in [-2,-1,0,1,2,3]:
    try:
        print(i/item)
    except ZeroDivisionError:
        print("infinite")
    
