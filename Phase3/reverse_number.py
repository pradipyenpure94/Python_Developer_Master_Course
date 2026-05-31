"""Reverse number."""


def reverse_number(num: int) -> int:
    """
    Return the reverse number.

    Args:
        num (int): Input number.

    Returns:
        int: Reversed number.
    """
    temp = abs(num)
    rev_num = 0

    while temp > 0:
        digit = temp % 10
        rev_num = rev_num * 10 + digit
        temp //= 10
    return rev_num if num >= 0 else -rev_num


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = reverse_number(num=number)
        print(f"Reversed number: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
