"""Read List from JSON File."""

import json

try:
    with open(file="file_handling/students_data.json", mode="r",
              encoding="utf-8") as file_obj:
        data = json.load(file_obj)
except FileNotFoundError:
    print("File does not exist.")
except json.decoder.JSONDecodeError:
    print("JSON format invalid.")
else:
    for record in data:
        print(record)
finally:
    print("Operation completed.")
