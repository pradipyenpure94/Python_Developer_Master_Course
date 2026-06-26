"""Search Record in JSON file."""

import json

try:
    name = input("Enter student name: ").strip()
    with open(file="file_handling/students_data.json", mode="r",
              encoding="utf-8") as file_obj:
        students = json.load(file_obj)

except FileNotFoundError:
    print("File does not exist.")
except json.JSONDecodeError:
    print("Invalid JSON file format.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    found = False
    for record in students:
        if record.get("name").casefold() == name.casefold():
            print(record)
            found = True

    if not found:
        print("Student record not found.")
finally:
    print("Operation completed.")
