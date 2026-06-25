"""Convert Dictionary to JSON String."""


import json

student = {
    "name": "Pradip",
    "age": 32,
    "city": "Pune",
}

json_string = json.dumps(student, indent=2, sort_keys=True)
print(json_string)
