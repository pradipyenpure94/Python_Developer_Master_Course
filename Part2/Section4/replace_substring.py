"""Replace substring."""


def validate_text(value: str, field_name: str) -> None:
    """
    Validate the user input text.
    """
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")


def replace_substring(
    text: str,
    old_substring: str,
    new_substring: str
) -> str:
    """
    Return a new string with all occurrences of the target substring
    replaced by the replacement text.

    Args:
        text (str): User input text.
        old_substring (str): Target substring.
        new_substring (str): Replacement substring.

    Returns:
        str: A modified string.
    """
    return text.replace(old_substring, new_substring)


def main() -> None:
    """Run the Main Program."""
    try:
        sentence = input("Enter the sentence: ").strip()
        validate_text(value=sentence, field_name="Text")
        target_substring = input("Enter the target substring: ").strip()
        validate_text(value=target_substring, field_name="Target substring")
        replacement_text = input("Enter the replacement text: ").strip()

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = replace_substring(
            text=sentence,
            old_substring=target_substring,
            new_substring=replacement_text
        )
        print(f"Modified string: {result}")


if __name__ == "__main__":
    main()
