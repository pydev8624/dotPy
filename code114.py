try:
    with open('test.txt','r') as f:
        text=f.read()
        print(text)
except Exception as e:
    print(e)
