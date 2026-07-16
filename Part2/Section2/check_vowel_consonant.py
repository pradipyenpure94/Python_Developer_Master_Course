"""Check vowel or consonant."""

from check_input import validate_char_length

VOWELS = {"a", "e", "i", "o", "u"}


def validate_alphabet_character(char: str) -> None:
    """Raise ValueError if character is not alphabets."""
    if not char.isalpha():
        raise ValueError("Please enter only alphabets.")


def main() -> None:
    """Run the Program."""
    try:
        character = input("Enter the character: ").strip()
        validate_char_length(char=character)
        validate_alphabet_character(char=character)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if character.lower() in VOWELS:
            print(f"'{character}' is a vowel.")
        else:
            print(f"'{character}' is a consonant.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
