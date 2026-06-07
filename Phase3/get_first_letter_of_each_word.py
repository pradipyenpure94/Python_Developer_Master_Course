"""Get first letter of each word."""


def get_first_letter_of_each_word(words: list[str]) -> list[str]:
    """
    Return new list containing the first letter of each word.

    Args:
        words (list[str]): Input words list.

    Returns:
        list[str]: A new list containing the first letter of each word.
    """
    return list(map(lambda word: word[0] if word else "", words))


if __name__ == "__main__":
    words = ["I", "Love", "you", ""]
    result = get_first_letter_of_each_word(words=words)
    print(f"First Letter of each word: {result}")
