import tempfile
import time

with open('fd\\test.png','rb') as f:
    img=f.read()

with tempfile.SpooledTemporaryFile(max_size=100, mode='w+b',dir='fd\\') as tmp:
    tmp.write(img)
    time.sleep(10)
    #tmp.seek(0)
    #print(tmp.read())
