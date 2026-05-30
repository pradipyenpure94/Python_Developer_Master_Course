"""Find maximum of three numbers."""


def find_max_number(num1: int, num2: int, num3: int) -> int:
    """
    Return the maximum of three numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.
        num3 (int): Third input number.

    Returns:
        int: Maximum of three input numbers.
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num1:
        return num2
    return num3


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        third_number = int(input("Enter third number: "))
        maximum_number = find_max_number(num1=first_number, num2=second_number,
                                         num3=third_number)
        print(f"Maximum number: {maximum_number}")
    except ValueError:
        print("Invalid input! Please enter a valid input.")
