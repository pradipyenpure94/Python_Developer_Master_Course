"""Read JSON file."""

import json
from pathlib import Path

FILE_PATH = Path("Part5/Phase6/sample_data.json")

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    result = json.load(file_obj)
    print(result)
