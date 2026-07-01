"""Count lines, words, and characters in a text file."""

from pathlib import Path

FILE_PATH = "Part1/sample_file.txt"

try:
    # Read entire .txt file.
    with open(file=FILE_PATH, mode="r",
              encoding="utf-8") as file_obj:

        content = file_obj.read()

except FileNotFoundError:
    file_name = Path(FILE_PATH).name
    print(f"{file_name} file does not exist.")
else:
    # No. of lines count in entire file.
    lines_count = len(content.splitlines())
    print(f"Lines count: {lines_count}")
    # Words count in entire file.
    words_count = len(content.split())
    print(f"Words count: {words_count}")
    # Characters count in entire file.
    characters_count = len(content)
    print(f"Characters count: {characters_count}")
finally:
    print("Operation completed.")
