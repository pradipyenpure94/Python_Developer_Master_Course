"""Flatten nested list."""

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [item for sublist in nested_list for item in sublist]
print(f"Flattened List: {flat_list}")
