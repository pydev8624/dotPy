try:
    with open('test.txt', 'r') as f:
        text = f.readlines()
        print(text)  # چاپ لیست اصلی (شامل \n)
        for item in text:
            print(item.strip())  # حذف \n از هر خط
except Exception as e:
    print(e)
