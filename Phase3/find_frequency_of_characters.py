"""Find frequency of characters."""


def find_frequency_of_characters(text: str) -> dict[str, int]:
    """
    Return the frequency of characters in string.

    Args:
        text (str): Input text.

    Returns:
        dict[str, int]: Frequency of characters.
    """
    freq = {}
    for char in text.casefold():
        freq[char] = freq.get(char, 0) + 1
    return freq


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = find_frequency_of_characters(text=input_text)
    print(f"Frequency of characters: {result}")
