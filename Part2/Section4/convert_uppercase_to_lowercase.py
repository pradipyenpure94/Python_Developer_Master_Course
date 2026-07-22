"""Convert uppercase to lowercase."""

from reverse_string import validate_string


def convert_to_lowercase(text: str) -> str:
    """
    Returns the lowercase text from the input string.

    Args:
        text (str): Input string.

    Returns:
        str: The input string converted to lowercase text.
    """
    return text.lower()


def main() -> None:
    """Run the Main Program."""
    try:
        input_string = input("Enter the input string: ").strip()
        validate_string(input_string=input_string)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = convert_to_lowercase(text=input_string)
        print(f"Lowercase text: {result}")


if __name__ == "__main__":
    main()
