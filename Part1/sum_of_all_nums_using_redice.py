"""Sum of all numbers using reduce()."""

from functools import reduce


def addition(nums: list[int]) -> int:
    """
    Return the sum of all numbers from the input list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: The sum of all numbers in the given list.
    """
    return reduce(lambda x, y: x + y, nums, 0)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(f"Input numbers: {numbers}")
    result = addition(nums=numbers)
    print(f"Addition: {result}")
