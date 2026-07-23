"""Find first non-repeating character."""

from reverse_string import validate_string


def find_first_non_repeating_character(text: str) -> str | None:
    """
    Return the first non-repeating character from the input string.
    Return None if no non-repeating character exists.

    Args:
        text (str): User input text.

    Returns:
        str | None: If the first non-repeating character is found,
        then return the character. Return None, if no non-repeating
        character exist.
    """
    freq = {}
    # Pass1
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Pass2
    for char in text:
        if freq[char] == 1:
            return char
    return None


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the text: ")
        validate_string(input_string=text)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = find_first_non_repeating_character(text=text)
        print(f"First non-repeating character: {result}")


if __name__ == "__main__":
    main()
