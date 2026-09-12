"""Iterate over a string using next() and iter()."""

text = "Pradip"

iterator = iter(text)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Error: StopIteration")
