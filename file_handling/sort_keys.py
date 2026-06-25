"""Sort Keys."""

import json

student = {
    "name": "Pradip",
    "age": 32,
    "salary": 150000,
}

# Sort JSON data keys.
json_string = json.dumps(student, indent=2, sort_keys=True)
print(json_string)
print(type(json_string))
