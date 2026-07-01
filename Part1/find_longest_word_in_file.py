"""Find the longest word in a file."""

from pathlib import Path

FILE_PATH = "Part1/sample_file.txt"

try:
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        file_obj_read = file_obj.read()
        words = file_obj_read.split()
        longest_word = max(words, key=len)
except FileNotFoundError:
    file_name = Path(FILE_PATH).name
    print(f"{file_name} does not exist.")
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Longest word: {longest_word}")
finally:
    print("Operation completed.")
