"""Longest word."""

from reverse_string import validate_string


def find_longest_word(text: str) -> str:
    """
    Return the longest word in the input text.

    Args:
        text (str): User input text.

    Returns:
        str: The longest word in the input text.
    """
    words = text.split()
    return max(words, key=len)


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
        result = find_longest_word(text=sentence)
        print(f"Longest word: {result}")


if __name__ == "__main__":
    main()
