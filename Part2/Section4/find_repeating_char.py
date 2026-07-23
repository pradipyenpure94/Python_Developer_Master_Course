"""Find first repeating character."""

from reverse_string import validate_string


def find_first_repeating_character(text: str) -> str | None:
    """
    Return the first repeating character. Return None
    if no repeating character exists.

    Args:
        text (str): User input text.

    Returns:
        str | None: The first repeating character, or None
        if no repeating character exists.
    """
    freq = {}

    # Pass 1
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Pass 2
    for char in text:
        if freq[char] > 1:
            return char
    return None


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
        result = find_first_repeating_character(text=text)
        print(f"First repeating character: {result}")


if __name__ == "__main__":
    main()
