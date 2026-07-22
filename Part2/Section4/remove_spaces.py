"""Remove spaces."""

from reverse_string import validate_string


def remove_spaces(text: str) -> str:
    """
    Return the input string with all whitespace removed.

    Args:
        text (str): User input string.

    Returns:
        str: The input string with all whitespace removed.
    """
    return "".join(char for char in text if not char.isspace())


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the string: ")
        validate_string(input_string=text)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = remove_spaces(text=text)
        print(f"After removing spaces: {result}")


if __name__ == "__main__":
    main()
