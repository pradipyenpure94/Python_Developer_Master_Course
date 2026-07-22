"""Count consonants."""

from reverse_string import validate_string


VOWELS = {
    "a",
    "e",
    "i",
    "o",
    "u",
}


def count_consonants(text: str) -> int:
    """
    Return the count of consonants in the input string.

    Args:
        text (str): User input string.

    Returns:
        int: Total number of consonants in the input string.
    """
    return sum(
        1 for char in text
        if char.isalpha() and char.casefold() not in VOWELS)


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
        result = count_consonants(text=text)
        print(f"Consonants count: {result}")


if __name__ == "__main__":
    main()
