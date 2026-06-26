"""Count Records in JSON File."""


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
    print(f"Student record count: {len(students)}")
finally:
    print("Operation completed.")
