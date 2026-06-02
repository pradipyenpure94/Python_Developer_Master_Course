"""Convert lowercase to uppercase."""


def to_uppercase(text: str) -> str:
    """
    Return the uppercase letters in string.

    Args:
        text (str): Input text.

    Returns:
        str: Uppercase letters in string.
    """
    return text.upper()


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = to_uppercase(text=input_text)
    print(f"Lowercase to uppercase letters: {result}")
