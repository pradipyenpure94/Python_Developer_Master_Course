"""Remove blank lines."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    for line in file_obj.readlines():
        if line.strip():
            print(line, end="")
