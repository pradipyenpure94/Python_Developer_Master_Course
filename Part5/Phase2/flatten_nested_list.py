"""Flatten a nested list."""


numbers = [[1, 2, 3], [4, 5, 6], [1, 4, 5]]

flatten = []

for sublist in numbers:
    flatten.extend(sublist)

print(f"Flatten List: {flatten}")
