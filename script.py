from pathlib import Path

current_dir=Path('.')
current_file=Path(__file__).name

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath == current_file:
        continue
    print (f" -{filepath.name}")

    
    if filepath.is_file():
        try:
            content = filepath.read_text(encoding='utf-8')
            print(f" Content: {content}")
        except Exception:
            print(" [Skipped non-text file]")