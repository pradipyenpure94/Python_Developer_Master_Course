"""Check whether number is strong or not."""

from math import factorial


def factorial_sum(num: int) -> int:
    """Return the factorial sum.

    Args:
        num (int): Input number.

    Returns:
        int: Sum of factorial of each digit in number.
    """
    total = 0
    for digit in str(num):
        total += factorial(int(digit))
    return total


def is_strong_number(num: int) -> bool:
    """
    Check whether number is a strong number or not.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is a strong number, otherwise False.
    """
    if num <= 0:
        raise ValueError("Number must be greater than zero.")
    return num == factorial_sum(num=num)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_strong_number(num=number):
            print(f"{number} is a strong number.")
        else:
            print(f"{number} is not a strong number")
    except ValueError as error:
        print(f"Error: {error}")
