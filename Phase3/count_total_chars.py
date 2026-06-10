"""Count total characters."""

from functools import reduce


def count_total_characters(text: str) -> int:
    """
    Return the total number of characters in the input string.

    Args:
        text (str): Input text.

    Returns:
        int: Total number of characters in the input string.
    """
    return reduce(lambda accumulator, _: accumulator + 1, text, 0)


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_total_characters(text=input_text)
    print(f"Count total characters: {result}")
