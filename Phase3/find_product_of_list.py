"""Find product of list."""

from functools import reduce
from operator import mul


def find_product_of_list(nums: list[int]) -> int:
    """
    Return the product of all numbers in the list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Product of all numbers in the list.
    """
    return reduce(mul, nums, 1)


if __name__ == "__main__":
    numbers = [0, 1, 2, 3, 4, 5]
    result = find_product_of_list(nums=numbers)
    print(f"Product of List: {result}")
