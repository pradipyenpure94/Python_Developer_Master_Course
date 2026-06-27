"""Find the largest of three numbers."""


def find_largest_number(num1: int, num2: int, num3: int) -> int:
    """
    Return the largest of the three input numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.
        num3 (int): Third input number.

    Returns:
        int: The largest of the three input numbers.
    """
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    return num3


if __name__ == "__main__":
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        third_number = int(input("Enter third number: "))
        result = find_largest_number(num1=first_number, num2=second_number,
                                     num3=third_number)
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram Interrupted.")
    else:
        print(f"Largest number: {result}")
    finally:
        print("Operation completed.")
