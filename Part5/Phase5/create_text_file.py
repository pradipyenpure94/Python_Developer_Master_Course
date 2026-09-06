"""Create text a file."""

from pathlib import Path

FILE_PATH = "Part5/Phase5/sample_text_file.txt"
file_name = Path(FILE_PATH).name

with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
    file_obj.write("Hello, Python")
    print(f"{file_name} file is  created successfully")
