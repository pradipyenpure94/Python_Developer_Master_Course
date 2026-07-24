"""Remove punctuation."""

from string import punctuation
from replace_substring import validate_text

TRANSLATOR = str.maketrans("", "", punctuation)


def remove_punctuation(text: str) -> str:
    """
    Return the normalized text without punctuation.

    Args:
        text (str): User input text.

    Returns:
        str: The normalized text without punctuation.
    """
    return text.translate(TRANSLATOR)


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the text: ").strip()
        validate_text(value=text, field_name="Text")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = remove_punctuation(text=text)
        print(f"Normalized text: {result}")


if __name__ == "__main__":
    main()
