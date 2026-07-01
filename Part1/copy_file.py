"""Copy contents from one file to another."""

from pathlib import Path

SRC_FILE_PATH = "Part1/sample_file.txt"
DEST_FILE_PATH = "Part1/sample_file1.txt"

try:
    # Read entire file.
    with open(file=SRC_FILE_PATH, mode="r",
              encoding="utf-8") as source_file_obj:
        content = source_file_obj.read()

except FileNotFoundError:
    file_name = Path(SRC_FILE_PATH).name
    print(f"{file_name} file does not exist.")
else:
    with open(file=DEST_FILE_PATH, mode="w",
              encoding="utf-8") as destination_file_obj:
        # Copy Sourc file content and write into destination file.
        destination_file_obj.write(content)
finally:
    print("Operation completed.")
