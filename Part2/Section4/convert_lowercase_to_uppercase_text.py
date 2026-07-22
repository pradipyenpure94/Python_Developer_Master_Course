"""Convert lowercase to uppercase."""

from reverse_string import validate_string


def to_uppercase(text: str) -> str:
    """
    Return the input string converted to uppercase.

    Args:
        text (str): User input string.

    Returns:
        str: The input string converted to uppercase.
    """
    return text.upper()


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
        result = to_uppercase(text=text)
        print(f"Uppercase text: {result}")


if __name__ == "__main__":
    main()
