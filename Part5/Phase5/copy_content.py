"""Copy contents from one file to another."""

from pathlib import Path

SOURCE_FILE_PATH = Path("Part5/Phase5/hello_world.txt")
DESTINATION_FILE_PATH = Path("Part5/Phase5/duplicate_copy_file.txt")

with open(file=SOURCE_FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    contents = file_obj.read()

with open(file=DESTINATION_FILE_PATH, mode="w", encoding="utf-8") as file_obj:
    file_obj.write(contents)
