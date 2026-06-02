"""Count vowels."""


def count_vowels(text: str) -> int:
    """Return the count of vowels in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of vowels in string.
    """
    vowels = "aeiou"
    return sum(1 for char in text.casefold() if char in vowels)


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_vowels(text=input_text)
    print(f"Count vowels: {result}")
