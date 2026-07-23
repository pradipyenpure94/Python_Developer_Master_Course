"""Check anagram."""

from collections import Counter
from reverse_string import validate_string


def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Check whether the two input strings are anagrams.

    Args:
        first_string (str): First input string.
        second_string (str): Second input string.

    Returns:
        bool: True, if both input strings are anagrams; otherwise, False.
    """
    if len(first_string) != len(second_string):
        return False
    return Counter(first_string.casefold()) == Counter(
        second_string.casefold()
    )


def main() -> None:
    """Run the Main Program."""
    try:
        first_string = input("Enter the first string: ").strip()
        validate_string(input_string=first_string)
        second_string = input("Enter the second string: ").strip()
        validate_string(input_string=second_string)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_anagram(first_string=first_string, second_string=second_string):
            print("The strings are anagrams.")
        else:
            print("The strings are not anagrams.")


if __name__ == "__main__":
    main()
