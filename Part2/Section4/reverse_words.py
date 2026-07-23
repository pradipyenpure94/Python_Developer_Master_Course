"""Reverse words."""

from reverse_string import validate_string


def reverse_words(text: str) -> str:
    """
    Return the reverse words from the input text.

    Args:
        text (str): User input text.

    Returns:
        str: The reversed words from the input text.
    """
    return " ".join(reversed(text.split()))


def main() -> None:
    """Run the Main Program."""
    try:
        sentence = input("Enter the sentence: ").strip()
        validate_string(input_string=sentence)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = reverse_words(text=sentence)
        print(f"Reversed words: {result}")


if __name__ == "__main__":
    main()
