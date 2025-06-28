import glob

files = glob.glob(pathname='*.*',root_dir='C:\\',recursive=True,include_hidden=True)
print(files)
files = glob.glob(pathname='*',root_dir='C:\\',recursive=True,include_hidden=True)
print(files)

