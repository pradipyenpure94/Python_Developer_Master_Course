"""Replace word in a file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")

old_word = "Python"
new_word = "DSA"

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    data = file_obj.read()

updated_contents = data.replace(old_word, new_word)

with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
    file_obj.write(updated_contents)
