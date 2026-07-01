"""Count frequency of each word in file."""

from pathlib import Path

FILE_PATH = "Part1/sample_file.txt"

try:
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        contents = file_obj.read().split()

except FileNotFoundError:
    file_name = Path(FILE_PATH).name
    print(f"{file_name} does not exist.")
else:
    if not contents:
        print("File is empty.")
    else:
        freq = {}
        for word in contents:
            freq[word] = freq.get(word, 0) + 1
        print(f"Count frequency of each word: {freq}")
finally:
    print("Operation completed.")
