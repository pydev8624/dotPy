import os

try:
    os.putenv('MY_VAR', '123')
except Exception as e:
    print(e)
