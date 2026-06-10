"""Concatenate strings."""

from functools import reduce


def concatenate_strings(words: list[str]) -> str:
    """
    Return a single string formed by concatenating all strings in the list.

    Args:
        words (list[str]): Input words list.

    Returns:
        str: A string containing all concatenated words.
    """
    return reduce(lambda x, y: x + y, words, "")


if __name__ == "__main__":
    input_words = ["I", "Love", "You"]
    result = concatenate_strings(words=input_words)
    print(f"Concatenate strings: {result}")
