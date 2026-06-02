"""Count consonants."""


def count_consonants(text: str) -> int:
    """Return the consonants in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of consonants in string.
    """
    vowels = "aeiou"
    input_text = text.casefold().strip()
    return sum(1 for char in input_text
               if char.isalpha() and char not in vowels)


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_consonants(text=input_text)
    print(f"Count consonants: {result}")
