try:
    file=open("text.txt","r")
    text=file.read()
    print(text)
    file.close()
except Exception as e:
    print(e)
