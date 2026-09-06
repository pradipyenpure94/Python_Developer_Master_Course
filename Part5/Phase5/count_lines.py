"""Count lines in a file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    lines = file_obj.readlines()
    print(f"Number of lines: {len(lines)}")
