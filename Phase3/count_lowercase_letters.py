"""Count lowercase letters."""


def count_lowercase_letters(text: str) -> int:
    """
    Return the count of lowercase letters in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of lowercase letters in string.
    """
    count = 0

    for char in text:
        if char.isalpha() and char.islower():
            count += 1
    return count


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_lowercase_letters(text=input_text)
    print(f"Count lowercase letters: {result}")
