"""Display file size."""

from os import path


try:
    file_size = path.getsize("file_handling/sample_text.txt")
    print(f"File size: {file_size}")
except FileNotFoundError:
    print("File does not exist.")
