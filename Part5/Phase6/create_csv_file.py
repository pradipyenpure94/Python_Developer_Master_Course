"""Create a CSV file."""

import csv
from pathlib import Path

FILE_PATH = Path("Part5/Phase6/sample_csv_file.csv")
fieldnames = ["name", "age"]

data = [
    {"name": "Pradip", "age": 33},
    {"name": "Amit", "age": 30}
]

with open(file=FILE_PATH, mode="w", newline="", encoding="utf-8") as file_obj:
    writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    print(f"{FILE_PATH.name} file is created successfully.")
