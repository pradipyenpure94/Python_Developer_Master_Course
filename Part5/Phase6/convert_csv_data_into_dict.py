"""Convert CSV data into dictionary."""

import csv
from pathlib import Path

FILE_PATH = Path("Part5/Phase6/student_marks.csv")

nested_data_dictionary = {}

with open(file=FILE_PATH, mode="r", encoding="utf-8", newline="") as file_obj:
    csv_reader = csv.DictReader(file_obj)

    for record in csv_reader:
        key = int(record["id"])
        nested_data_dictionary[key] = record

print(nested_data_dictionary)
