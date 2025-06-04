try:
    with open('test.txt','r') as f:
        text=f.readline()
        print(text)
except Exception as e:
    print(e)
