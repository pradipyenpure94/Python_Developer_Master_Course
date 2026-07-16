"""Check alphabet, digit or special character."""

CHARACTER_LENGTH = 1


def validate_char_length(char: str) -> None:
    """Validate the character length."""
    if len(char) != CHARACTER_LENGTH:
        raise ValueError("Input must contain exactly one character.")


def main() -> None:
    """Run the character classification program."""
    try:
        character = input("Enter the input character: ").strip()
        validate_char_length(char=character)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if character.isdigit():
            print(f"{character} is digit.")
        elif character.isalpha():
            print(f"{character} is alphabet.")
        else:
            print(f"{character} is special character.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
