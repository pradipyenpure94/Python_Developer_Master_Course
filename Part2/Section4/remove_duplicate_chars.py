"""Remove duplicate characters."""

from reverse_string import validate_string


def remove_duplicate_characters(text: str) -> str:
    """
    Remove duplicate characters from the input string and
    return the modified string.

    Args:
        text: User input text.

    Returns:
        str: The output will be a new string that has duplicate characters
        removed from the input string.
    """
    return "".join(dict.fromkeys(text))


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
        result = remove_duplicate_characters(text=text)
        print(f"After removing duplicate characters: {result}")


if __name__ == "__main__":
    main()
