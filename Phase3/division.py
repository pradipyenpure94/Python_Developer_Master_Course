"""Division of two numbers."""


def divide_numbers(num1: int, num2: int) -> float:
    """Return the division of two numbers.
    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        float: Division of two numbers.
    """
    return num1 / num2


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        print(f"Division: {divide_numbers(num1=first_number,
              num2=second_number)}")
    except (ZeroDivisionError, ValueError):
        print("Invalid input! Please enter a valid input.")
