"""Create JSON data."""

import json

user_data = [
    {
        "id": 101, "name": "Pradip",
    },
    {
        "id": 102, "name": "Amit",
    }
]

result = json.dumps(user_data, indent=2)
print(result)
