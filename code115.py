try:
    with open('test.txt','w') as f:
        text="it is python"
        f.write(text)
except Exception as e:
    print(e)
