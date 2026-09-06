"""Search a word in a file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    search_word = "Python"

    if search_word in file_obj.read():
        print(f"'{search_word}' word found in '{FILE_PATH.name}' file.")
    else:
        print(f"'{search_word}' not found in '{FILE_PATH.name}' file.")
