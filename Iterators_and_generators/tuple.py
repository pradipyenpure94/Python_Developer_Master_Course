"""Iterate over a tuple using next() and iter()."""

my_tuple = (10, 20, 30, 40, 50)

iterator = iter(my_tuple)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("Iterator is exhausted.")
