try:
    a=int(input())
    b=int(input())
    print(a/b)
except (ZeroDivisionError,ValueError) as e:
    print(e)

    
