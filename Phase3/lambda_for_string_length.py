"""Lambda for string length."""


def string_length(text: str) -> int:
    """
    Return the length of a string.

    Args:
        text (str): Input text.

    Returns:
        int: Length of the string.
    """
    length = lambda string: len(string)
    return length(text)


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = string_length(text=input_text)
    print(f"Length of string: {result}")
