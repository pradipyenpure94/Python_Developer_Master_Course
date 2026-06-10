"""Find longest word."""

from functools import reduce


def find_longest_word(words: list[str]) -> str | None:
    """
    Return a longest word from the list.

    Args:
        words (list[str]): Input words list.

    Returns:
        str | None: The longest word in the list, or None if the list empty.
    """
    if not words:
        return None
    return reduce(lambda x, y: x if len(x) > len(y) else y, words)


if __name__ == "__main__":
    input_words = ["Ram", "Pradip", "Amit", "yenpure", "Rajendra"]
    result = find_longest_word(words=input_words)
    print(f"Longest word: {result}")
