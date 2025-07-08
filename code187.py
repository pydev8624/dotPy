from pathlib import Path

for item in Path('fd\\').iterdir():
    print(item)
