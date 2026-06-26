"""Delete Record from JSON File."""

import json

try:
    with open(file="file_handling/students_data.json", mode="r",
              encoding="utf-8") as file_obj:
        students = json.load(file_obj)
    students = [record for record in students if record.get('id') != 3]
except FileNotFoundError:
    print("File does not exist.")
except json.JSONDecodeError:
    print("Invalid JSON file format.")
else:
    with open(file="file_handling/students_data.json", mode="w",
              encoding="utf-8") as file_obj:
        json.dump(students, file_obj, indent=2)
    print("Deleted record successfully.")
finally:
    print("Operation completed.")
