"""Check GCD."""

from math import gcd


def find_gcd(num1: int, num2: int) -> int:
    """
    Return the GCD of two numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Greatest common divisor number.
    """
    num1 = abs(num1)
    num2 = abs(num2)

    return gcd(num1, num2)


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        result = find_gcd(num1=first_number, num2=second_number)
        print(f"GCD of {first_number} and {second_number} is: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
