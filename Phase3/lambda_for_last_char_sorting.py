"""Lambda for last character sorting."""


def last_character_sort(words: list[str]) -> list[str]:
    """
    Return a list sorted by the last character of each word.
    Args:
        words (list[str]): Input words list.
    Returns:
        list[str]: List sorted by the last character of each word.
    """
    return sorted(words, key=lambda word: word[-1] if word else "")


if __name__ == "__main__":
    input_words = ["apple", "banana", "kiwi", "cherry", "grape", ""]
    result = last_character_sort(words=input_words)
    print(f"List sorted by last char: {result}")
