i=int(input("number : "))
try:
    for item in [-2,-1,0,1,2,3]:
        print(i/item)
except ZeroDivisionError:
    print("Infinite")
