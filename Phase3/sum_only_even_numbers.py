"""Sum only even numbers."""

from functools import reduce
from operator import add


def find_sum_only_even_numbers(nums: list[int]) -> int:
    """
    Return the sum of even numbers only.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Sum of all even numbers in the list, or 0 if the list is empty or
                contains no even numbers.
    """
    return reduce(add, filter(lambda num: num % 2 == 0, nums), 0)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = find_sum_only_even_numbers(nums=numbers)
    print(f"Sum of Even numbers: {result}")
