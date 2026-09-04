"""Function to check palindrome."""

from reverse_string import reverse_string


def is_palindrome(text: str) -> bool:
    """Check whether a string is palindrome."""
    text = text.casefold()
    return text == reverse_string(text=text)


if __name__ == "__main__":
    try:
        text = input("Enter the string: ").strip()
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_palindrome(text=text):
            print("String is a palindrome.")
        else:
            print("String is not a palindrome.")
