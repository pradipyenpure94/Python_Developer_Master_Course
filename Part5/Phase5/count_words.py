"""Count words in a file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    word_count = 0

    for line in file_obj.readlines():
        word_count += len(line.split())

    print(f"Word Count: {word_count}")
