"""Find substring."""

from reverse_string import validate_string


def find_substring(text: str, sub_string: str) -> bool:
    """
    Check whether the given substring is found in the input text.

    Args:
        text (str): User input text.
        sub_string (str): User input substring.

    Returns:
        bool: True if the substring is found; otherwise, False.
    """
    return sub_string in text


def main() -> None:
    """Run the Main Program."""
    try:
        sentence = input("Enter the sentence: ").strip()
        validate_string(input_string=sentence)
        sub_string = input("Enter the sub string: ").strip()
        validate_string(input_string=sub_string)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if find_substring(text=sentence, sub_string=sub_string):
            print(f"{sub_string} is found in {sentence}.")
        else:
            print(f"{sub_string} is not found in {sentence}.")


if __name__ == "__main__":
    main()
