"""Count digits in a number."""


def count_digits_in_number(num: int) -> int:
    """
    Return the digits count of the input number.

    Args:
        num (int): Input number.

    Returns:
        int: Count of a digits of the input number.
    """
    temp = abs(num)
    digits_count = 0

    if temp == 0:
        return 1

    while temp > 0:
        digits_count += 1
        temp //= 10
    return digits_count


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = count_digits_in_number(num=number)
        print(f"Count of digits of the input number {number}: {result}")
    finally:
        print("Operation completed.")
