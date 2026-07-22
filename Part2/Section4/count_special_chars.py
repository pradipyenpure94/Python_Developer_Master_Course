"""Count special characters."""

from reverse_string import validate_string


def count_special_characters(text: str) -> int:
    """
    Return the total count of special characters in the input string.

    Args:
        text (str): User input string.

    Returns:
        int: Total count of special characters in the input string.
    """
    return sum(1 for char in text if not char.isalnum() and not char.isspace())


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
        result = count_special_characters(text=text)
        print(f"Total count of special characters: {result}")


if __name__ == "__main__":
    main()
