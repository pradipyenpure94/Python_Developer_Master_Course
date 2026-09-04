"""Remove duplicate values from dictionary."""

data = {"p": 2, "r": 1, "a": 1, "d": 1, "i": 1}

unique_data_vals = {}
seen_data_vals = set()

for key, val in data.items():
    if val not in seen_data_vals:
        seen_data_vals.add(val)
        unique_data_vals[key] = val

print(f"Unique data values: {unique_data_vals}")
