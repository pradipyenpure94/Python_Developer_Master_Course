"""Convert uppercase to lowercase."""


def to_lowercase(text: str) -> str:
    """
    Return the lowercase letters in string.

    Args:
        text (str): Input text.

    Returns:
        str: Lowercase letters in string.
    """
    return text.lower()


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = to_lowercase(text=input_text)
    print(f"Convert uppercase to lowercase letters: {result}")
