"""Create nested tuple."""

nested_tuple = tuple((number, number ** 2) for number in range(1, 6))
print(f"Nested tuple: {nested_tuple}")
