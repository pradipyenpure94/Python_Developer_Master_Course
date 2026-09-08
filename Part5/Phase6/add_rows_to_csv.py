"""Add rows to CSV."""


import csv
from pathlib import Path

field_names = ["id", "name"]

FILE_PATH = Path("Part5/Phase6/add_rows.csv")

data = [
    {"id": 101, "name": "Pradip"},
    {"id": 102, "name": "Pranali"}
]

with open(file=FILE_PATH, mode="w", encoding="utf-8", newline="") as file_obj:
    writer = csv.DictWriter(file_obj, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)
