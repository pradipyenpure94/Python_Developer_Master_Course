"""Find sum of digits."""


def sum_of_digits(num: int) -> int:
    """
    Return the sum of the digits of the input number.

    Args:
        num (int): Input number.

    Returns:
        int: Sum of digits of an input number.
    """
    total = 0
    temp = abs(num)

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10
    return total


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = sum_of_digits(num=number)
        print(f"Sum of the digits of {number}: {result}")
    finally:
        print("Operation completed.")
