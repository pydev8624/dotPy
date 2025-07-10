import tempfile
import os
import time

with tempfile.TemporaryDirectory(dir='fd\\') as tmpdir:
    print("Temporary directory path:", tmpdir)
    filepath = os.path.join(tmpdir, "example.txt")
    with open(filepath, 'w') as f:
        f.write("Inside temporary directory.")
    with open(filepath, 'r') as f:
        print(f.read())
    time.sleep(10) 

