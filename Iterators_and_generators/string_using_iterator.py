"""Iterate through string using iterator."""

name = "PYTHON"

iterator = iter(name)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
