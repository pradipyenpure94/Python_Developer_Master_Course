"""Recursive GCD"""


def find_gcd_number(num1: int, num2: int) -> int:
    """
    Return the greatest common divisor (GCD) of two numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Greatest common divisor (GCD) of two input numbers.
    """
    num1 = abs(num1)
    num2 = abs(num2)

    if num1 == 0 and num2 == 0:
        raise ValueError("GCD is undefined when both numbers are zero.")

    if num2 == 0:
        return num1
    return find_gcd_number(num1=num2, num2=num1 % num2)


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        result = find_gcd_number(num1=first_number, num2=second_number)
        print(f"GCD of number: {result}")
    except ValueError as error:
        print(f"Error: {error}")
