"""Create single string from list."""

from functools import reduce


def create_single_string_from_list(words: list[str]) -> str:
    """
    Return the single string formed by joining all words in the list.

    Args:
        words (list[str]): Input words list.

    Returns:
        str: A single string containing all words separated by spaces.
    """
    return reduce(lambda x, y: f"{x} {y}" if x else y, words, "")


if __name__ == "__main__":
    input_words = ["Pradip", "Rajendra", "Yenpure"]
    result = create_single_string_from_list(words=input_words)
    print(f"String: {result}")
