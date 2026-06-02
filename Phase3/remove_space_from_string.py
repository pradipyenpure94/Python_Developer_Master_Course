"""Remove spaces from string."""


def remove_space_from_string(text: str) -> str:
    """Remove spaces from string.

    Args:
        text (str): Input text.

    Returns:
        str: Removed space from string.
    """
    return "".join(char for char in text if not char.isspace())


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = remove_space_from_string(text=input_text)
    print(f"Removed space from string: {result}")
