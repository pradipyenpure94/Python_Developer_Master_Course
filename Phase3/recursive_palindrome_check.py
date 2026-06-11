"""Recursive palindrome check."""


def is_palindrome(text: str) -> bool:
    """
    Check whether a string is a palindrome.

    Args:
        text (str): Input text.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text=text[1:-1])


if __name__ == "__main__":
    input_text = input("Enter a text: ")
    if is_palindrome(text=input_text):
        print(f"{input_text} is a palindrome string.")
    else:
        print(f"{input_text} is not a palindrome string.")
