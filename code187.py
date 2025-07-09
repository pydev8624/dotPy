from pathlib import Path

filez = []
folderz = []

p = Path('fd')

for item in p.iterdir():
    if item.is_file():
        filez.append(str(item))
    elif item.is_dir():
        folderz.append(str(item))

print('\n')
print( filez)
print('\n')
print( folderz)
