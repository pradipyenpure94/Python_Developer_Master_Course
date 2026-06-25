"""Update JSON Record."""


import json

try:
    with open(file="file_handling/students_data.json", mode="r",
              encoding="utf-8") as file_obj:
        data = json.load(file_obj)

except FileNotFoundError:
    print("File does not exist.")
except json.JSONDecodeError:
    print("Invalid JSON file format.")
else:
    # Update record into JSON file.
    found = False
    for record in data:
        if record.get("id") == 3:
            record["age"] = 28
            found = True
            break

    with open(file="file_handling/students_data.json", mode="w",
              encoding="utf-8") as file_obj:
        json.dump(data, file_obj, indent=4)
    if found:
        print("Data updated successfully.")
    else:
        print("Record not found.")
finally:
    print("Operation completed.")
