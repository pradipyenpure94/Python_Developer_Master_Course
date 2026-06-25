"""Pretty Print JSON."""

import json

student = {
    "name": "Pradip",
    "age": 32,
    "city": "Pune",
}

# Convert Python object data to a JSON string.
json_string = json.dumps(student, indent=3)
print(json_string)
print(type(json_string))
