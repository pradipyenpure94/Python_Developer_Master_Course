"""Recursive palindrome check."""


def is_palindrome(text: str) -> bool:
    """Check whether a string is palindrome."""
    if len(text) <= 1:
        return True

    if text[0] == text[-1]:
        return is_palindrome(text=text[1:-1])

    return False


if __name__ == "__main__":
    text = input("Enter the string: ").strip()
    if is_palindrome(text=text):
        print(f"{text} is a palindrome.")
    else:
        print(f"{text} is not a palindrome.")
