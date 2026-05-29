"""Multiplication of two numbers."""


def multiply_numbers(num1: int, num2: int) -> int:
    """Multiplication of two numbers.
    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Multiplication of two numbers.
    """
    return num1 * num2


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        print(f"Multiplication: {multiply_numbers(num1=first_number,
              num2=second_number)}")
    except ValueError:
        print("Invalid input! Please enter a valid input.")
