from pathlib import Path

base = Path('fd\\ab.txt')
target=Path('fd\\test\\asd.txt')

print(base.replace(target))
