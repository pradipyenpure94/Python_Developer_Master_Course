"""Count vowels."""


def count_vowels(text: str) -> int:
    """Return the count of vowels in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of vowels in string.
    """
    vowels = "aeiou"
    count = 0
    i = 0
    input_text = text.casefold().strip()

    while i < len(input_text):
        char = input_text[i]
        if char in vowels:
            count += 1
        i += 1
    return count


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_vowels(text=input_text)
    print(f"Count vowels: {result}")
