"""Sum of digits."""


def sum_of_digits(num: int) -> int:
    """
    Return the sum of digits in number.

    Args:
        num (int): Input number.

    Returns:
        int: Sum of digits in number.
    """
    temp = abs(num)
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10
    return total


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = sum_of_digits(number)
        print(f"Sum of digits in number: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
