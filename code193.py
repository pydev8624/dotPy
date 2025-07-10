import tempfile
import time

with tempfile.TemporaryFile(mode='w+t',dir='fd\\') as tmp:
    tmp.write("Hello temporary file!")
    tmp.seek(0)
    print(tmp.read())  
    time.sleep(10)

