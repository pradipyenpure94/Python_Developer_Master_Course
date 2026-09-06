"""Merge two text files."""

from pathlib import Path

# Merge file path
MERGE_TEXT_FILE_PATH = Path("Part5/Phase5/merge_file.txt")
# Source file one
TEXT_FILE1_PATH = Path("Part5/Phase5/hello_world.txt")
# Source file one
TEXT_FILE2_PATH = Path("Part5/Phase5/sample_text_file.txt")

SOURCE_FILES = [TEXT_FILE1_PATH, TEXT_FILE2_PATH]

with open(file=MERGE_TEXT_FILE_PATH, mode="w", encoding="utf-8") as file_obj:
    for fname in SOURCE_FILES:
        with open(file=fname, mode="r", encoding="utf-8") as infile:
            data = infile.read()
            file_obj.write(data)
            file_obj.write("\n")
