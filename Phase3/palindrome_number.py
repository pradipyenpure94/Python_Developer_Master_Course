"""Palindrome number."""


def reverse_number(num: int) -> int:
    """
    Return the reverse number.

    Args:
        num (int): Input number.

    Returns:
        int: Reversed number.
    """
    temp = num
    rev_number = 0
    while temp > 0:
        digit = temp % 10
        rev_number = rev_number * 10 + digit
        temp //= 10
    return rev_number


def is_palindrome_number(num: int) -> bool:
    """
    Check whether number is palindrome or not.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is a palindrome, otherwise False.
    """
    if num < 0:
        raise ValueError("Palindrome number cannot be negative.")
    return num == reverse_number(num=num)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_palindrome_number(num=number):
            print(f"{number} is a palindrome number.")
        else:
            print(f"{number} is not a palindrome number.")
    except ValueError as error:
        print(f"Error: {error}")
