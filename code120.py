try:
    with open('test.txt', 'r') as f:
        text = f.readlines()
        print(text)
except Exception as e:
    print(e)
