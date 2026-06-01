"""Check plaindrome string."""

from reverse_string import reverse_string


def is_palindrome_string(text: str) -> bool:
    """
    Check whether string is a palindrome or not.

    Args:
        text (str): Input text.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    return text == reverse_string(text=text)


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    if is_palindrome_string(text=input_text):
        print(f"{input_text} is a palindrome string.")
    else:
        print(f"{input_text} is not a palindrome string.")
