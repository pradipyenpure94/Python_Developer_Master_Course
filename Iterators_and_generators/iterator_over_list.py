"""Iterate over list using iter() and next()."""

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Error: StopIteration")
