from pathlib import Path

p = Path('fd\\a.txt')

p.rename(p.with_name('abc.py'))


