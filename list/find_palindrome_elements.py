"""Find the palindrome elements in list."""

data = [121, 141, 123, 456, 454, "ram", "Madam", "racecar",
        True, False, 3.14, 9.8, -464]

filtered_data = [item for item in data if isinstance(item, (int, str)) and
                 not isinstance(item, bool)]


def is_palindrome_number(number: int) -> bool:
    """Check whether a number is palindrome
    Args:
        number (int): input number
    Returns:
        bool: True if number is palindrome otherwise False
    """
    if number < 0:
        return False

    temp = number
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10
    return number == reversed_number


def is_palindrome_string(text: str) -> bool:
    """Check whether a string is palindrome
    Args:
        text (str): input string
    Returns:
        bool: True if string is palindrome otherwise False
    """
    temp = text.strip().casefold()
    reversed_string = "".join(reversed(temp))
    return temp == reversed_string


palindrome_items = []

for item in filtered_data:
    if isinstance(item, str):
        if is_palindrome_string(item):
            palindrome_items.append(item)
    elif isinstance(item, int):
        if is_palindrome_number(item):
            palindrome_items.append(item)

print(f"Palindrome items: {palindrome_items}")
