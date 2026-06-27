"""Reverse an integer."""


def reverse_number(num: int) -> int:
    """
    Return the reverse number of the given input number.

    Args:
        num (int): Input number.

    Returns:
        int: Reversed number.
    """
    temp = abs(num)
    reversed_num = 0

    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10

    return reversed_num if num > 0 else reversed_num * -1


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = reverse_number(num=number)
        print(f"Reversed number: {result}")
    finally:
        print("Operation completed.")
