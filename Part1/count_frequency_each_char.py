"""Count frequency of each character."""


def count_character_frequency(text: str) -> dict[str, int]:
    """
    Return the frequency of each character.

    Args:
        text (str): Input text.

    Returns:
        dict[str, int]: Dictionary mapping each character to its frequency.
    """
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


if __name__ == "__main__":
    try:
        input_text = input("Enter a string: ").strip()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        frequency_count = count_character_frequency(text=input_text)
        print(f"Count of frequency of each character: {frequency_count}")
    finally:
        print("Operation completed.")
