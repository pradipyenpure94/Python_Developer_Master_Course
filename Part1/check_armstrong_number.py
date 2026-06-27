"""Check whether a number is a Armstrong."""


def count_digit_number(num: int) -> int:
    """
    Return the digit count of the input number.

    Args:
        num (int): Input number.

    Returns:
        int: Digit count.
    """
    temp = num
    digit_count = 0

    if temp == 0:
        return 1

    while temp > 0:
        digit_count += 1
        temp //= 10
    return digit_count


def is_armstrong_number(num: int) -> bool:
    """
    Check whether a number is an Armstrong.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is an Armstrong, otherwise False.
    """
    if num < 0:
        raise ValueError("Armstrong numbers are not defined for negative numbers.")

    power = count_digit_number(num=num)
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return num == total


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_armstrong_number(num=number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        print("Operation completed.")
