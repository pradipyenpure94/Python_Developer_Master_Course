"""Iterator with dictionary."""

data = {"name": "Pradip", "age": 33}

# Iteratar with dictionary values
iterator = iter(data.values())

print(next(iterator))
print(next(iterator))

# Iteratar with dictionary items()
iterator = iter(data.items())

print(next(iterator))
print(next(iterator))

# Iteratar with dictionary keys()
iterator = iter(data.keys())

print(next(iterator))
print(next(iterator))
