import glob

files = glob.glob(pathname='*.txt')
print(files)
print("\n")


files = glob.glob(pathname='?.txt')
print(files)
print("\n")

files = glob.glob(pathname='[ab].txt')
print(files)
print("\n")

files = glob.glob(pathname='[!ab].txt')
print(files)
print("\n")

files = glob.glob(pathname='[!abc].txt')
print(files)
print("\n")

files = glob.glob(pathname='???.txt')
print(files)
print("\n")
