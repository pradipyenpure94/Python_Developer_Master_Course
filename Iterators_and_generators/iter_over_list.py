"""Iterate over list using next() and iter()."""

fruits = ["apple", "banana", "cherry", "jackfruit"]

iterator = iter(fruits)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Error: StopIteration")
