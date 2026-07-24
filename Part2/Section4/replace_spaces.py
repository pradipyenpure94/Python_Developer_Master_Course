"""Replace spaces."""

from reverse_string import validate_string

REPLACEMENT_CHARACTER_LENGTH_LIMIT = 1


def validate_replacement_character(character: str) -> None:
    """Validate the replacement character."""
    if not character:
        raise ValueError("Character cannot be empty.")
    if len(character) != REPLACEMENT_CHARACTER_LENGTH_LIMIT:
        raise ValueError(
            "The replacement character must be exactly"
            f"{REPLACEMENT_CHARACTER_LENGTH_LIMIT} character(s) long."
        )


def replace_spaces(text: str, replacement_character: str) -> str:
    """
    Return a new string with all spaces replaced by the replacement character.

    Args:
        text (str): User input text.
        replacement_character (str): A specific character.

    Returns:
        str: A new modified string,
        with all spaces replaced by the replacement character.
    """
    return text.replace(" ", replacement_character)


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the string: ").strip()
        validate_string(input_string=text)
        replacement_char = input("Enter a replacement character: ").strip()
        validate_replacement_character(character=replacement_char)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = replace_spaces(
            text=text,
            replacement_character=replacement_char
        )
        print(f"Modified string: {result}")


if __name__ == "__main__":
    main()
