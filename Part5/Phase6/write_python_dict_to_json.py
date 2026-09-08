"""Write Python Dictionary into JSON."""

import json
from pathlib import Path

FILE_PATH = Path("Part5/Phase6/sample_data.json")

data = {
    "name": "Pradip",
    "age": 33
}

with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
    json.dump(data, file_obj, indent=4)
