"""Add New Record in JSON File."""

import json


try:
    with open(file="file_handling/students_data.json", mode="r",
              encoding="utf-8") as file_obj:
        data = json.load(file_obj)

except FileNotFoundError:
    print("File does not exist.")
except json.JSONDecodeError:
    print("Invalid JSON format.")
else:
    new_student = {
        "name": "Pranjal",
        "age": 27,
        "city": "Bangalore"
    }

    data.append(new_student)

    with open(file="file_handling/students_data.json", mode="w",
              encoding="utf-8") as file_obj:
        json.dump(data, file_obj, indent=3)

    print("Data written successfully.")
finally:
    print("Operation completed.")
