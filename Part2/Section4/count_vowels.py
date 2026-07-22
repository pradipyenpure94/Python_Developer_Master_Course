"""Count vowels."""

from reverse_string import validate_string


VOWELS = {
    "a",
    "e",
    "i",
    "o",
    "u",
}


def count_vowels(text: str) -> int:
    """
    Calculate and return the count of vowels from the input string.

    Args:
        text (str): User input string.

    Returns:
        int: Total number of vowels in the input string.
    """
    return sum(1 for char in text if char.casefold() in VOWELS)


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
        result = count_vowels(text=text)
        print(f"Vowels count: {result}")


if __name__ == "__main__":
    main()
