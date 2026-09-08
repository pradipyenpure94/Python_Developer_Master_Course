"""calculate average marks from CSV."""

import csv
from pathlib import Path

FIELD_NAMES = ["id", "name", "marks"]
FILE_PATH = Path("Part5/Phase6/student_marks.csv")

data = [
    {"id": 101, "name": "Pradip", "marks": 96},
    {"id": 102, "name": "Pranjal", "marks": 69},
    {"id": 103, "name": "Pranali", "marks": 85}
]

with open(file=FILE_PATH, mode="w", newline="", encoding="utf-8") as file_obj:
    csv_writer = csv.DictWriter(file_obj, fieldnames=FIELD_NAMES)
    csv_writer.writeheader()
    csv_writer.writerows(data)

total_marks = 0
total_students = 0

with open(file=FILE_PATH, mode="r", encoding="utf-8", newline="") as file_obj:
    csv_reader = csv.DictReader(file_obj)
    for record in csv_reader:
        total_marks += float(record["marks"])
        total_students += 1

if total_students == 0:
    print("No students available.")
else:
    print(f"Total Marks    : {total_marks:.2f}")
    print(f"Total Students : {total_students}")
    average_marks = total_marks / total_students
    print(f"Average Marks  : {average_marks:.2f}")
