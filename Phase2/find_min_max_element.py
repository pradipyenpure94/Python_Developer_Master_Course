"""Find minimum and maximum element"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if numbers:
    min_number = reduce(lambda x, y: x if x < y else y, numbers)
    max_number = reduce(lambda x, y: x if x > y else y, numbers)

    print(f"Minimum element: {min_number}")
    print(f"Maximum element: {max_number}")
else:
    print("List is empty!")
