import glob

pat=glob.escape('[file*??.*]')
info=glob.glob(pat)
print(info)

pat=glob.escape('[file*??.**]')
info=glob.glob(pat)
print(info)
