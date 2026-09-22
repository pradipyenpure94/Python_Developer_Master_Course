"""Create an iterator from a list."""

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("StopIteration")
