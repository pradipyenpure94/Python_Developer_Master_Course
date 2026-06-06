"""Lambda for palindrome check."""


def is_palindrome(text: str) -> bool:
    """
    Check whether string is a palindrome.

    Args:
        text (str): Input string.

    Returns:
        bool: True if string is a palindrome, Otherwise False.
    """
    result = lambda string: string.casefold() == string[::-1].casefold()
    return result(text)


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    if is_palindrome(text=input_text):
        print(f"{input_text} is a palindrome.")
    else:
        print(f"{input_text} is not a palindrome.")
