"""Count uppercase letter."""


def count_uppercase_letter(text: str) -> int:
    """
    Return the count of uppercase letter in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of uppercase letters in string.
    """
    count = 0
    index = 0

    while index < len(text):
        char = text[index]
        if char.isalpha() and char.isupper():
            count += 1

        index += 1

    return count


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_uppercase_letter(text=input_text)
    print(f"Count uppercase letters: {result}")
