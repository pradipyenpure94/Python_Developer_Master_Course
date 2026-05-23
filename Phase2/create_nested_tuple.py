"""Create nested tuple."""

nested_list = []
number = 1

while number < 6:
    nested_list.append((number, number ** 2))
    number += 1

nested_tuple = tuple(nested_list)
print(f"Nested tuple: {nested_tuple}")
