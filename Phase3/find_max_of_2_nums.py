"""Find maximum of two numbers."""


def find_max_number(num1: int, num2: int) -> int:
    """
    Return the maximum of two numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Maximum number.
    """
    if num1 > num2:
        return num1
    return num2


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        maximum_number = find_max_number(num1=first_number, num2=second_number)
        print(f"Maximum number: {maximum_number}")
    except ValueError:
        print("Invalid input! Please enter a valid input.")
