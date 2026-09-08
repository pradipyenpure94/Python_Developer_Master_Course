"""Read CSV file."""

import csv
from pathlib import Path

FILE_PATH = Path("Part5/Phase6/sample_csv_file.csv")

with open(file=FILE_PATH, mode="r", encoding="utf-8", newline="") as file_obj:
    reader = csv.DictReader(file_obj)
    for record in reader:
        print(record)
