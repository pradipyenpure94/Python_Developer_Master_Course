"""Write JSON Data into file."""

import json


data = {
    "name": "Pradip",
    "age": 32,
    "city": "Pune",
    "salary": 150000,
}

with open(file="file_handling/student_data.json", mode="w",
          encoding="utf-8") as file_obj:
    json.dump(data, file_obj, indent=4)
    print("Data written successfully.")
