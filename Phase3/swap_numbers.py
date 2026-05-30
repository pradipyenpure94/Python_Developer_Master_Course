"""Swap two numbers using function."""


def swap_two_numbers(num1: int, num2: int) -> tuple[int, int]:
    """Return the two numbers after swapping their values.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        tuple[int, int]: Swapped numbers.
    """
    num1, num2 = num2, num1
    return num1, num2


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        first_number, second_number = swap_two_numbers(num1=first_number, num2=second_number)
        print("After swapped numbers:")
        print(f"First number: {first_number}")
        print(f"Second number: {second_number}")
    except ValueError:
        print("Invalid input! Please enter an integer number.")
