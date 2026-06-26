"""Nested JSON Example."""

import json


try:
    with open(file="file_handling/students_data.json", mode="r",
              encoding="utf-8") as file_obj:
        students = json.load(file_obj)

except FileNotFoundError:
    print("File does not exist.")
except json.JSONDecodeError:
    print("Invalid JSON file format.")
else:
    # Student name
    for record in students:
        print(f"Student: {record['name']}")
        # Subject name student wise
        for index, subject in enumerate(record['subject'], start=1):
            print(f"{index}: {subject}")
finally:
    print("Operation completed.")
