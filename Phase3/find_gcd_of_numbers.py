"""Find GCD of numbers."""

from functools import reduce
from math import gcd


def find_gcd_number(nums: list[int]) -> int | None:
    """
    Return the GCD of all numbers in the list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int | None: GCD of all numbers, or None if the list is empty.
    """
    if not nums:
        return None
    return reduce(gcd, nums)


if __name__ == "__main__":
    numbers = [48, 64, 80]
    numbers = []
    result = find_gcd_number(nums=numbers)
    print(f"GCD of number: {result}")
