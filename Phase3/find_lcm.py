"""Find LCM."""

from math import lcm


def find_lcm(num1: int, num2: int) -> int:
    """Return the LCM of two numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: LCM of two numbers.
    """
    return lcm(num1, num2)


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        result = find_lcm(num1=first_number, num2=second_number)
        print(f"LCM of {first_number} and {second_number} is: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
