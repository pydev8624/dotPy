import tempfile

with tempfile.NamedTemporaryFile(mode='w+t') as tmp:
    print("Temporary filename:", tmp.name)
    tmp.write("This file has a name!")
    tmp.seek(0)
    print(tmp.read())

