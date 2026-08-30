"""Find the intersection of multiple lists."""

from collections import Counter
from functools import reduce

numbers = [[1, 2, 3], [2, 3, 1], [4, 1, 5]]
common_counter = reduce(lambda a, b: Counter(a) & Counter(b), numbers)
common_elements = list(common_counter.keys())
print(f"Common Elements: {common_elements}")
