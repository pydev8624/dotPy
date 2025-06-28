import glob

for items in glob.iglob(pathname='*.*',root_dir='C:\\',recursive=True,include_hidden=True):
    print(items)
print('\n')
for items in  glob.iglob(pathname='*',root_dir='C:\\',recursive=True,include_hidden=True):
    print(items)

