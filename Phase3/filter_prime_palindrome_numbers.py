"""Filter palindrome numbers."""


def is_palindrome(num: int) -> bool:
    """
    Check whether a number is a palindrome.

    Args:
        num (int): Input number.

    Returns:
        bool: True, if number is a palindrome, otherwise False.
    """
    if num < 0:
        return False

    rev_num = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        rev_num = rev_num * 10 + digit
        temp //= 10
    return num == rev_num


def filter_palindrome_numbers(nums: list[int]) -> list[int]:
    """
    Return a new palindrome numbers list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing the palindrome numbers.
    """
    return list(filter(is_palindrome, nums))


if __name__ == "__main__":
    numbers = [101, 102, 103, 404, 405, 606]
    result = filter_palindrome_numbers(nums=numbers)
    print(f"Palindrome numbers: {result}")
