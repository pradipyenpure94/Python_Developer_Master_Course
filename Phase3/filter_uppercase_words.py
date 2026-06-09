"""Filter uppercase words."""


def filter_uppercase_words(words: list[str]) -> list[str]:
    """
    Return a new list containing the uppercase words.

    Args:
        words (list[str]): Input words list.

    Returns:
        list[str]: A new list containing the uppercase words.
    """
    return list(filter(str.isupper, words))


if __name__ == "__main__":
    input_words = ["pradip", "AMIT", "Lahu", "UMESH"]
    result = filter_uppercase_words(words=input_words)
    print(f"Uppercase words: {result}")
