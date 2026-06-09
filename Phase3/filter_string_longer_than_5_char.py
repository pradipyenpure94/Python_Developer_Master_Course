"""Filter strings longer than 5 chars."""


def filter_strings_more_than_5_chars(words: list[str]) -> list[str]:
    """
    Return new list containing strings more than 5 chars.

    Args:
        words (list[str]): Input words list.

    Returns:
        list[str]: A new list containing the strings more than 5 chars.
    """
    return list(filter(lambda word: len(word) > 5, words))


if __name__ == "__main__":
    input_words = ["Pradip", "Amit", "jay", "lahu", "Aakash"]
    result = filter_strings_more_than_5_chars(words=input_words)
    print(f"Filter strings more than 5 chars: {result}")
