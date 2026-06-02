"""Count words in string."""


def count_words(text: str) -> int:
    """
    Return the count of words in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of words in string.
    """
    return sum(1 for word in text.split())


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = count_words(text=sentence)
    print(f"Count of words: {result}")
