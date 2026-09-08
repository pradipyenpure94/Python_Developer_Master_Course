"""Update JSON data."""

import json
from pathlib import Path

FILE_PATH = Path("Part5/Phase6/sample_data.json")


with open(file=FILE_PATH, mode="r", encoding="utf-8", newline="") as file_obj:
    read_data = json.load(file_obj)
read_data.update({"name": "Swaraj", "age": 29, "gender": "Male"})

with open(file=FILE_PATH, mode="w", encoding="utf-8", newline="") as file_obj:
    json.dump(read_data, file_obj, indent=4)
