"""Filter special characters."""


def remove_special_chars(text: str) -> str:
    """
    Return a new string with all non-alphanumeric characters removed.

    Args:
        text (str): Input text.

    Returns:
        str: A string containing only alphanumeric characters.
    """
    return "".join(filter(str.isalnum, text))


if __name__ == "__main__":
    input_text = "Hello, @pradip12!, how are you?"
    result = remove_special_chars(text=input_text)
    print(f"Remove special chars from text: {result}")
