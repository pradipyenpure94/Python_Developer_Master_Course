"""Neon number."""


def is_neon_number(num: int) -> bool:
    """
    Check whether number is a neon number or not.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is a neon number, otherwise False.
    """
    if num < 0:
        raise ValueError("Number must be non-negative.")

    square = num ** 2
    total = sum(int(number) for number in str(square))
    return num == total


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_neon_number(num=number):
            print(f"{number} is a neon number.")
        else:
            print(f"{number} is not a neon number.")
    except ValueError as error:
        print(f"Error: {error}")
