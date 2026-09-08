"""Search user from JSON."""

import json
from pathlib import Path

FILE_PATH = Path("Part5/Phase6/sample_data.json")

search_name = "swaraj".casefold()

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    read_data = json.load(file_obj)
    if read_data["name"].casefold() == search_name:
        print("Name found.")
    else:
        print("Name not found.")
