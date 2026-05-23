"""Create nested tuple."""

nested_list = []

for number in range(1, 6):
    nested_list.append((number, number ** 2))

nested_tuple = tuple(nested_list)
print(f"Nested tuple: {nested_tuple}")
