"""Find length of each word."""


def find_length_each_word(words: list[str]) -> list[int]:
    """
    Return the length of each word from list.

    Args:
        words (list(str)): Input words list.

    Returns:
        list[int]: Length of each word.
    """
    return list(map(lambda word: len(word), words))


if __name__ == "__main__":
    words = ["one", "two", "three", "four", "five"]
    result = find_length_each_word(words=words)
    print(f"Length of each word: {result}")
