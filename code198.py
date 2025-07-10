import tempfile
import os
import time

fd, path = tempfile.mkstemp(dir='fd\\')
try:
    with os.fdopen(fd, 'w') as tmp:
        tmp.write("Using mkstemp")
    with open(path, 'r') as f:
        print(f.read())
finally:
    time.sleep(10)
    os.remove(path)  # حذف دستی
