"""Count character frequency."""

from collections import Counter
from reverse_string import validate_string


def count_characters_frequency(text: str) -> dict[str, int]:
    """
    Return a new dictionary with the characters and
    their frequency from the input string.

    Args:
        text: User input text.

    Returns:
        dict[str, int]: Return a new dictionary with the characters and
        their frequency from the input string.
    """
    return dict(Counter(text))


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the string: ")
        validate_string(input_string=text)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("Operation cancelled by the user.")
    else:
        result = count_characters_frequency(text=text)
        print(f"Count characters frequency: {result}")


if __name__ == "__main__":
    main()
