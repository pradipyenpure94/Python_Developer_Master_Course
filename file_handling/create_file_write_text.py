"""Create a text file and write content into it."""

from pathlib import Path

# Create directory if not exists
Path("file_handling").mkdir(exist_ok=True)

# Open file in write mode
with open("file_handling/sample_text.txt", mode="w",
          encoding="utf-8") as file_obj:
    file_obj.write("Hello Python...!!")
