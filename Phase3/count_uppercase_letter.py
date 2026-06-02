"""Count uppercase letter."""


def count_uppercase_letter(text: str) -> int:
    """
    Return the count of uppercase letter in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of uppercase letters in string.
    """
    return sum(1 for char in text if char.isalpha() and char.isupper())


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_uppercase_letter(text=input_text)
    print(f"Count uppercase letters: {result}")
