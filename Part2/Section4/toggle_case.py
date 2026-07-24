"""Toggle case."""

from reverse_string import validate_string


def toggle_case_text(text: str) -> str:
    """
    Return a new string with the case of each alphabetic character toggled.

    Args:
        text (str): User input text.

    Returns:
        str: A new string with the case of each alphabetic character toggled.

    """
    return text.swapcase()


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
        result = toggle_case_text(text=text)
        print(f"Toggled text: {result}")


if __name__ == "__main__":
    main()
