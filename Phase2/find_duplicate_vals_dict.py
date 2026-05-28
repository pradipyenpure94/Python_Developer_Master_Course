"""Find duplicate values in dictionary."""

data = {"a": 1, "b": 1, "c": 2, "d": 3, "e": 3}

data_values = list(data.values())
duplicates = {value
              for value in data_values
              if data_values.count(value) > 1}
print(f"Duplicate values in dictionary: {duplicates}")
