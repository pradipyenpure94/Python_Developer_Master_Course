"""Append data to a file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")
FILE_NAME = FILE_PATH.name

with open(file=FILE_PATH, mode="a", encoding="utf-8") as file_obj:
    content = "My target is achieving 20 LPA salary package."
    file_obj.write(content + "\n")
    print(f"Content appended to {FILE_NAME} successfully.")
