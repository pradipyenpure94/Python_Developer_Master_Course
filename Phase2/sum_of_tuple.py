"""Find sum of tuple elements."""

from functools import reduce

numbers = (1, 2, 3, 4, 5, 6)
total = reduce(lambda x, y: x + y, numbers, 0)
print(f"Sum of numbers (tuple): {total}")
