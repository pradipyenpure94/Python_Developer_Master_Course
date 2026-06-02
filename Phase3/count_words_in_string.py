"""Count words in string."""


def count_words(text: str) -> int:
    """
    Return the count of words in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of words in string.
    """
    count = 0

    for _ in text.split():
        count += 1
    return count


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = count_words(text=sentence)
    print(f"Count of words: {result}")
