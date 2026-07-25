"""Compress string."""

from itertools import groupby
from replace_substring import validate_text


def compress_string(text: str) -> str:
    """
    Return the Run-Length-Encoding (RLE) representation of the input text.

    Args:
        text (str): User input text.

    Returns:
        str: The compressed string.
    """
    compressed = []
    for character, group in groupby(text):
        count = sum(1 for _ in group)
        compressed.append(f"{character}{count}")
    return "".join(compressed)


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the string: ").strip()
        validate_text(value=text, field_name="Text")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = compress_string(text=text)
        print(f"Compressed string: {result}")


if __name__ == "__main__":
    main()
