"""Count words."""

from reverse_string import validate_string


def count_words(text: str) -> int:
    """
    Return the count of words from the input text.

    Args:
        text (str): User input text.

    Returns:
        int: The count of words.
    """
    return len(text.split())


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
        result = count_words(text=text)
        print(f"Count of words: {result}")


if __name__ == "__main__":
    main()
