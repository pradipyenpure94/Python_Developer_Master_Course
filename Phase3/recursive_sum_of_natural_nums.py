"""Recursive sum of natural numbers."""


def sum_of_natural_numbers(num: int) -> int:
    """
    Return the sum of natural numbers up to the given number.

    Args:
        num (int): Input number.

    Returns:
        int: Sum of natural numbers from 1 to num.
    """
    if num < 0:
        raise ValueError("Number must be greater than or equal to zero.")
    if num == 0:
        return 0
    return num + sum_of_natural_numbers(num - 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = sum_of_natural_numbers(num=number)
        print(f"Sum of natural number: {result}")
    except ValueError as error:
        print(f"{error}")
