"""Sum of all elements in list."""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = reduce(lambda x, y: x + y, numbers)
print(f"Sum of List: {total}")
