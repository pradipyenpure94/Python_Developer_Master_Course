"""Find duplicate values in dictionary."""

data = {"a": 1, "b": 1, "c": 2, "d": 3, "e": 3}

seen = set()

data_values = data.values()
duplicates = {value for value in data_values
              if value in seen or seen.add(value)}
print(f"Duplicate values in dictionary: {duplicates}")
