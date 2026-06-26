"""Find Student with Highest Age."""

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
    try:
        oldest = max(students, key=lambda x: x.get("age", 0))
    except ValueError:
        print("Empty data.")
    else:
        print(f"Student with Highest Age: {oldest}")
finally:
    print("Operation completed.")
