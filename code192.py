from pathlib import Path

p=Path('fd\\c.txt')

text=p.read_text()
print(text)

p.write_text('hello python ')

i=Path('fd\\test.png')
c=i.read_bytes()

j=Path('fd\\copy.png')
j.write_bytes(c)




