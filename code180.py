import fnmatch

print(fnmatch.fnmatchcase('abc.txt', '??c.txt'))
print(fnmatch.fnmatchcase('abC.txt', '??c.txt'))


