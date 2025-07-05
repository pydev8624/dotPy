import fnmatch

names = ['file.txt', 'data.csv', 'image.png', 'file.csv']
print(fnmatch.filter(names, '*.csv'))
