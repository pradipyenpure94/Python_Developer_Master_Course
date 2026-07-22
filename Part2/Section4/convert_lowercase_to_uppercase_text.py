"""Convert lowercase to uppercase."""

from reverse_string import validate_string
from convert_uppercase_to_lowercase import UPPERCASE_TO_LOWERCASE

LOWERCASE_TO_UPPERCASE = {
    val: key for key, val in UPPERCASE_TO_LOWERCASE.items()
}


def to_uppercase(text: str) -> str:
    """
    Return the input string converted to uppercase.

    Args:
        text (str): User input string.

    Returns:
        str: The input string converted to uppercase.
    """
    return "".join(LOWERCASE_TO_UPPERCASE.get(char, char) for char in text)


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
