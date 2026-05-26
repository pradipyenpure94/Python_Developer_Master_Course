"""Group duplicate values."""

from itertools import groupby

data = [1, 1, 2, 3, 1, 4, 5, 2, 4, 8]

sorted_data = sorted(data)
grouped = []

for _, group in groupby(sorted_data):
    group_list = list(group)
    if len(group_list) > 1:
        grouped.append(group_list)

print(f"Duplicate groups values: {grouped}")
