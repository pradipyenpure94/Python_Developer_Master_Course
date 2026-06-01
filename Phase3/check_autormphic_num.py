"""Automorphic number."""


def is_automorphic_number(num: int) -> bool:
    """
    Check whether number is an automorphic number or not.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is an automorphic number, otherwise False.
    """
    if num < 0:
        raise ValueError("Number must be non-negative.")
    square = num ** 2
    return str(square).endswith(str(num))


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_automorphic_number(num=number):
            print(f"{number} is an automorphic number.")
        else:
            print(f"{number} is not an automorphic number.")
    except ValueError as error:
        print(f"Error: {error}")
