"""Recursive digit sum."""


def sum_digits(num: int) -> int:
    """
    Return the sum of all digits in a number.

    Args:
        num (int): Input number.

    Returns:
        int: Sum of all digits in the number.
    """
    num = abs(num)
    # Base case: if the remaining number is 0, stop recursion.
    if num == 0:
        return 0
    # Recursive case: last digit + sum of the remaining digits.
    return (num % 10) + sum_digits(num=num // 10)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = sum_digits(num=number)
        print(f"Sum of digits: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
