"""Word frequency."""

from string import punctuation
from reverse_string import validate_string

TRANSLATOR = str.maketrans("", "", punctuation)


def get_word_frequency(text: str) -> dict[str, int]:
    """
    Return the word frequency from the input text.

    Args:
        text (str): User input text.

    Returns:
        dict[str, int]: The word frequency from the input text.
    """
    clean_text = text.translate(TRANSLATOR)
    words = clean_text.casefold().split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


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
        result = get_word_frequency(text=sentence)
        print(f"Word frequency: {result}")


if __name__ == "__main__":
    main()
