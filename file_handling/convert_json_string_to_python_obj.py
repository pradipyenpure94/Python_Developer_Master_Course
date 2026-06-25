"""Convert JSON string to python object."""

import json

json_string = '{"name": "Pradip", "age": 32, "city": "Pune"}'

data = json.loads(json_string)
print(data)

print(type(data))
