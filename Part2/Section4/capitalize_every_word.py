"""Capitalize every word."""

from reverse_string import validate_string


def capitalize_every_word(text: str) -> str:
    """
    Return the new string with every word's first letter
    capitalized and the rest lowercase.

    Args:
        text (str): User input text.

    Returns:
        str: The new string with the first letter of each word capitalized and
        the remaining letters are converted to lowercase.
    """
    return text.title()


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the string: ").strip()
        validate_string(input_string=text)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = capitalize_every_word(text=text)
        print(f"Modified string: {result}")


if __name__ == "__main__":
    main()
