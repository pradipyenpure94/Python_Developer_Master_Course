"""Remove duplicate characters."""


def remove_duplicate_chars(text: str) -> str:
    """
    Return the unique characters in string.

    Args:
        text (str): Input text.

    Returns:
        str: Unique characters string.
    """
    unique_characters = []
    seen = set()
    for char in text.casefold():
        if char.isalpha() and char not in seen:
            unique_characters.append(char)
            seen.add(char)
    return "".join(unique_characters)


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = remove_duplicate_chars(text=input_text)
    print(f"Unique characters: {result}")
