"""Find largest digit."""

from functools import reduce


def find_largest_digit(num: int) -> int:
    """
    Return the largest digit in the given number.

    Args:
        num (int): Input number.

    Returns:
        int: Largest digit in the given number.
    """
    return reduce(lambda x, y: x if x > y else y, map(int, str(abs(num))))


if __name__ == "__main__":
    number = 15234
    result = find_largest_digit(num=number)
    print(f"Largest digit: {result}")
