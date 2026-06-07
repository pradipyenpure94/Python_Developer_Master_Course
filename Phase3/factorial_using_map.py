"""Apply factorial using map."""

from math import factorial


def get_factorial_numbers(nums: list[int]) -> list[int]:
    """
    Return a new list containing the factorial of each number.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing the factorial of each number.
    """
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("All values must be integers.")
    if any(num < 0 for num in nums):
        raise ValueError("All numbers must be non-negative.")
    return list(map(factorial, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = get_factorial_numbers(nums=numbers)
    print(f"Factorial numbers: {result}")
