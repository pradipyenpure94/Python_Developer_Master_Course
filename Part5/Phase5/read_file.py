"""Read complete file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")
FILE_NAME = FILE_PATH.name

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    content = file_obj.read()
    print(content)
    print(f"{FILE_NAME} file content read successfully.")
