import tempfile
import time

with tempfile.NamedTemporaryFile(mode='w+t',dir='fd\\') as tmp:
    print("Temporary filename:", tmp.name)
    tmp.write("This file has a name!")
    tmp.seek(0)
    print(tmp.read())
    time.sleep(10)
