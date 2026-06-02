"""Count digits in string."""


def count_digits(text: str) -> int:
    """
    Return the count of digits in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of digits in string.
    """
    return sum(1 for char in text if char.isdigit())


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_digits(text=input_text)
    print(f"Count of digits: {result}")
