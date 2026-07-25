"""Decompress string."""

from replace_substring import validate_text


def validate_compressed_string(text: str) -> None:
    """Validate the compressed string format."""
    index = 0

    while index < len(text):
        character = text[index]
        index += 1

        if index >= len(text) or not text[index].isdigit():
            raise ValueError(f"Missing count after character '{character}'.")

        start = index
        while index < len(text) and text[index].isdigit():
            index += 1

        count = int(text[start:index])
        if count <= 0:
            raise ValueError(
                f"Count for character '{character}' must be greater than zero."
            )


def decompress_string(text: str) -> str:
    """
    Return the Run-Length-Encoding (RLE) input.

    Args:
        text (str): Compressed RLE string.

    Returns:
        str: The decompressed string.
    """
    decompressed = []
    index = 0

    while index < len(text):
        character = text[index]
        index += 1

        start = index
        while index < len(text) and text[index].isdigit():
            index += 1

        count = int(text[start:index])
        decompressed.append(character * count)

    return "".join(decompressed)


def main() -> None:
    """Run the Main Program."""
    try:
        text = input("Enter the string: ").strip()
        validate_text(value=text, field_name="Text")
        validate_compressed_string(text=text)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = decompress_string(text=text)
        print(f"Decompressed string: {result}")


if __name__ == "__main__":
    main()
