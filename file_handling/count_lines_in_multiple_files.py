"""Count lines in multiple files."""

from pathlib import Path


# Multiple file names
files = ["file_handling/file11.txt", "file_handling/file2.txt"]
for file_name in files:
    try:
        base_file_name = Path(file_name).name
        with open(file=file_name, mode="r", encoding="utf-8") as file_obj:
            # Display file name and line count
            print(f"{base_file_name}: {sum(1 for _ in file_obj)}")
    except FileNotFoundError:
        print(f"{base_file_name} file does not exist.")
