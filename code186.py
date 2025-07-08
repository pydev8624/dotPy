from pathlib import Path

p = Path('fd\\c.txt')
print(p.is_file())  # True if it's a file

d = Path('fd\\')
print(d.is_dir())   # True if it's a directory
