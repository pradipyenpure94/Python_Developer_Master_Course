"""Check uppercase/lowercase."""

CHARACTER_LENGTH = 1


def validate_char_length(character: str) -> None:
    """Raise ValueError if not character length one."""
    if len(character) != CHARACTER_LENGTH:
        raise ValueError("Please enter exactly one character.")


def validate_input_character(character: str) -> None:
    """Raise ValueError if not an alphabet character."""
    if not character.isalpha():
        raise ValueError("Invalid Input. Please enter only alphabets.")


def main() -> None:
    """Run the Program."""
    try:
        char = input("Enter the character: ").strip()
        validate_char_length(character=char)
        validate_input_character(character=char)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if char.isupper():
            print(f"'{char}' is an uppercase character.")
        else:
            print(f"'{char}' is in lowercase character.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
