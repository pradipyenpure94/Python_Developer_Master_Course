"""Iterate through string using iterator."""

name = "PYTHON"

iterator = iter(name)
i = 0

while i < len(name):
    print(next(iterator))
    i += 1
