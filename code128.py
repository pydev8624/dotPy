import sys

if sys.platform=="linux":
    print("Linux")
elif sys.platform == "darwin":
    print("macOS")
elif sys.platform == "win32":
    print("Windows")
else:
    print("Unknown OS")
