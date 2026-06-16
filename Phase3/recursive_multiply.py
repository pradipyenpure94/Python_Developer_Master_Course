"""Recursive multiply."""


def multiply(num1: int, num2: int) -> int:
    """
    Return the multiplication of two numbers using recursion.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Multiplication of two numbers.
    """
    if num2 < 0:
        return -multiply(num1=num1, num2=-num2)

    if num2 == 0:
        return 0

    return num1 + multiply(num1=num1, num2=num2 - 1)


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        result = multiply(num1=first_number, num2=second_number)
        print(f"Multiplication: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
