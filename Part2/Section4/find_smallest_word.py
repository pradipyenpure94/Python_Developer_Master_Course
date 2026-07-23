"""Smallest word."""

from reverse_string import validate_string


def find_smallest_word(text: str) -> str:
    """
    Return the smallest word in the input text.

    Args:
        text (str): User input text.

    Returns:
        str: The smallest word in the input text.
    """
    words = text.split()
    return min(words, key=len)


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
        result = find_smallest_word(text=sentence)
        print(f"Smallest word: {result}")


if __name__ == "__main__":
    main()
