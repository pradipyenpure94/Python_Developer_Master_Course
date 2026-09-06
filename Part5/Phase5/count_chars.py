"""Count characters in a file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    data = file_obj.read()
    count_characters = sum(1 for char in data if not char.isspace())
    print(f"Count characters: {count_characters}")
