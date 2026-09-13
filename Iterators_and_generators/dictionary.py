"""Iterate through dictionary keys and values."""

data = {"name": "Pradip", "age": 33}

# Iterate through dictionary keys

iterators = iter(data)

print(next(iterators))
print(next(iterators))

# Iterate through dictinary values

iterators = iter(data.values())

print(next(iterators))
print(next(iterators))

# Iterate through dictionary items()

iterators = iter(data.items())

print(next(iterators))
print(next(iterators))
