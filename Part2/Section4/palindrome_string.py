"""Palindrome string."""

from reverse_string import reverse_string, validate_string


def is_palindrome(input_string: str) -> bool:
    """
    Check whether the input string is a palindrome.

    Args:
        input_string (str): User input string.

    Returns:
        bool: True if the input string is a palindrome; otherwise, False.
    """
    lower_text = input_string.casefold()
    return lower_text == reverse_string(input_string=lower_text)


def main() -> None:
    """Run the Main Program."""
    try:
        input_string = input("Enter the string: ").strip()
        validate_string(input_string=input_string)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_palindrome(input_string=input_string):
            print(f"{input_string} is a palindrome string.")
        else:
            print(f"{input_string} is not a palindrome string.")


if __name__ == "__main__":
    main()
