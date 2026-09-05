"""Use reduce() to calculate product."""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)
print(f"Result: {product}")
