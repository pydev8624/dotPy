try:
    with open('test.txt', 'r') as f:
        text = f.readlines()
        #print(text)
    with open('story.txt','w') as s:
        s.writelines(text)
except Exception as e:
    print(e)
