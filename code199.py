import tempfile
import os
import shutil
import time

path = tempfile.mkdtemp(dir='fd\\')
print("Temp directory:", path)


file_path = os.path.join(path, "temp.txt")
with open(file_path, 'w') as f:
    f.write("Manual deletion required.")

time.sleep(10)
shutil.rmtree(path)
