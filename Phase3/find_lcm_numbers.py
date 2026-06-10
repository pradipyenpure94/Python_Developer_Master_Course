"""Find LCM of numbers."""

from math import lcm
from functools import reduce


def find_lcm_numbers(nums: list[int]) -> int | None:
    """
    Return the lcm of all numbers in the list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int | None: LCM of all numbers in the list,
                    or None if the list is empty."""
    if not nums:
        return None
    return reduce(lcm, nums)


if __name__ == "__main__":
    numbers = [16, 80, 64]
    result = find_lcm_numbers(nums=numbers)
    print(f"LCM of number: {result}")
