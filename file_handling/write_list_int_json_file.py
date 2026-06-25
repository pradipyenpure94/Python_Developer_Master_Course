"""Write List into JSON File."""

import json

students = [
    {"name": "Pradip", "age": 32, "city": "Bangalore"},
    {"name": "Amit", "age": 30, "city": "Pune"},
]

with open(file="file_handling/students_data.json", mode="w",
          encoding="utf-8") as file_obj:
    json.dump(students, file_obj, indent=2)

print("Data written successfully.")
