"""Convert lowercase to uppercase."""


def convert_lowercase_to_uppercase(text: str) -> str:
    """
    Return lowercase to uppercase letters.

    Args:
        text (str): Input text.

    Returns:
        str: Uppercase letters.
    """
    return "".join(map(str.upper, text))


if __name__ == "__main__":
    word = input("Enter a word: ")
    result = convert_lowercase_to_uppercase(text=word)
    print(f"Uppercase text: {result}")
