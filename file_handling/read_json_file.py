"""Read JSON File."""

import json

try:
    with open(file="file_handling/student_data.json", mode="r",
              encoding="utf-8") as file_obj:

        # Read data from JSON file.
        data = json.load(file_obj)

except FileNotFoundError:
    print("File does not exist.")
except json.decoder.JSONDecodeError:
    print("Invalid JSON format.")
else:
    print(data)
    print(type(data))
finally:
    print("Operation completed.")
