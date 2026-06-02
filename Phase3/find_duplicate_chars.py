"""Find duplicate characters in string."""


def find_duplicate_characters(text: str) -> set[str]:
    """
    Return the duplicate characters from string.

    Args:
        text (str): Input text.

    Returns:
        set[str]: Duplicate characters set.
    """
    seen = set()
    duplicate_chars = set()

    for char in text.casefold():
        if char.isalpha():
            if char in seen:
                duplicate_chars.add(char)
            seen.add(char)
    return duplicate_chars


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = find_duplicate_characters(text=input_text)
    print(f"Duplicate characters: {result}")
