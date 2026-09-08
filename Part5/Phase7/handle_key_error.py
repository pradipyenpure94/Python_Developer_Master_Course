"""Handle Key Error."""

data = {"name": "Pradip", "age": 33}

try:
    result = data["age"]
except KeyError as error:
    print(f"Error: {error}")
else:
    print(f"Result: {result}")
