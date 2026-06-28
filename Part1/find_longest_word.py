"""Find longest word in a sentence."""


def find_longest_word(text: str) -> str:
    """
    Return the longest word from the input sentence.

    Args:
        text (str): Input sentence.

    Returns:
        str: The longest word in the input sentence.
    Raises:
        ValueError: If the input sentence contains no words.
    """
    words = text.split()

    if not words:
        raise ValueError("Input text cannot be empty.")

    return max(words, key=len)


if __name__ == "__main__":
    try:
        sentence = input("Enter the sentence: ").strip()
        result = find_longest_word(text=sentence)
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Longest word: {result}")
    finally:
        print("Operation completed.")
