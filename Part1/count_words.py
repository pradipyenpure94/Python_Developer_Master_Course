"""Count words in a sentence."""


def count_words(sentence: str) -> int:
    """
    Return the count of words in sentence.

    Args:
        sentence (str): Input text.

    Returns:
        int: Count of words in sentence.
    """
    words = sentence.split()
    return len(words)


if __name__ == "__main__":
    try:
        text = input("Enter the sentence: ").strip()

    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = count_words(sentence=text)
        print(f"Words count: {result}")
    finally:
        print("Operation completed.")
