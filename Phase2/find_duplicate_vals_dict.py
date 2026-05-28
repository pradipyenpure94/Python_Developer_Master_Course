"""Find duplicate values in dictionary."""

data = {"a": 1, "b": 1, "c": 2, "d": 3, "e": 3}

seen = set()
duplicates = set()

for value in data.values():
    if value in seen:
        duplicates.add(value)
    seen.add(value)

print(f"Duplicate values in dictionary: {duplicates}")
