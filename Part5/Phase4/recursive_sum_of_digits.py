"""Recursive sum of digits."""


def recursive_sum_digits(number: int) -> int:
    """
    Return the sum of digits using recursive function call.

    Args:
        number (int): Input number.

    Returns:
        int: The Sum of digits in number.
    """
    number = abs(number)

    if number == 0:
        return 0

    return number % 10 + recursive_sum_digits(number=number // 10)


if __name__ == "__main__":
    try:
        number = int(input("Enter the number: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        sum_of_digits = recursive_sum_digits(number=number)
        print(f"Sum of Digits: {sum_of_digits}")
