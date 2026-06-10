"""Multiply all odd numbers."""

from functools import reduce
from operator import mul


def multiply_odd_numbers(nums: list[int]) -> int:
    """
    Return the product of all odd numbers in the list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Product of all odd numbers in the list,
                    or 1 if the list is empty or contains no odd numbers.
    """
    return reduce(mul, filter(lambda num: num % 2 == 1, nums), 1)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = []
    result = multiply_odd_numbers(nums=numbers)
    print(f"Multiply all odd numbers: {result}")
