"""Handle FileNotFound Error."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase7/handle_key_error.py")

try:
    with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
        file_obj.read()
except FileNotFoundError as error:
    print(f"Error: {error}")
