"""Harshad number."""

from sum_of_digits import sum_of_digits


def is_harshad_number(num: int) -> bool:
    """
    Check whether number is a harshad number or not.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is a harshad number, otherwise False.
    """
    if num <= 0:
        raise ValueError("Number must be greater than zero.")
    total = sum_of_digits(num=num)
    return num % total == 0


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_harshad_number(num=number):
            print(f"{number} is a harshad number.")
        else:
            print(f"{number} is not a harshad number.")
    except ValueError as error:
        print(f"{error}")
