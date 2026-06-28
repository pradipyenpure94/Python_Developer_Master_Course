"""Check whether a string is palindrome."""

from reverse_string import reverse_string


def is_palindrome_string(text: str) -> bool:
    """
    Check whether a string is a palindrome.

    Args:
        text (str): Input text.

    Returns:
        bool: True if the string is a palindrome, otherwise False.
    """
    return text.casefold() == reverse_string(text=text).casefold()


if __name__ == "__main__":
    try:
        input_text = input("Enter a text: ").strip()

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        if is_palindrome_string(text=input_text):
            print(f"{input_text} is a palindrome string.")
        else:
            print(f"{input_text} is not a palindrome string.")
    finally:
        print("Operation completed.")
