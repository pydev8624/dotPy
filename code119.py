try:
    with open('test.png','rb') as img:
        image=img.read()
    with open('newtest.png','wb') as img:
        img.write(image)
except Exception as e:
    print(e)
