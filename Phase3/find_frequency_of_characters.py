"""Find frequency of characters."""


def find_frequency_of_characters(text: str) -> dict[str, int]:
    """
    Return the frequency of each character in string.

    Args:
        text (str): Input text.

    Returns:
        dict[str, int]: Mapping of characters to thier frequencies.
    """
    freq = {}
    index = 0
    input_text = text.casefold()

    while index < len(input_text):
        char = input_text[index]
        freq[char] = freq.get(char, 0) + 1

        index += 1

    return freq


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = find_frequency_of_characters(text=input_text)
    print(f"Frequency of characters: {result}")
