"""Find sum of list."""

from functools import reduce
from operator import add


def find_sum_of_list(nums: list[int]) -> int:
    """
    Return the sum of all numbers in the list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Sum of all numbers in the list.
    """
    return reduce(add, nums, 0)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    result = find_sum_of_list(nums=numbers)
    print(f"Sum of list: {result}")
