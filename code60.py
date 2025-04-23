lst1=[1,2,5,6,7,3,2,5,6,7,2,5]

print(lst1.index(2))

# طراحی تابعی برای مشخص کردن تمام ایندکس هایی که مقدار مورد نظر در لیست هست
def indexer(lst,v):
    for i in range(0,len(lst)-1):
        if lst[i]==v:
            print(i)

indexer(lst=lst1, v=2)

