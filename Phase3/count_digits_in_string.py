"""Count digits in string."""


def count_digits(text: str) -> int:
    """
    Return the count of digits in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of digits in string.
    """
    count = 0
    index = 0

    while index < len(text):
        char = text[index]
        if char.isdigit():
            count += 1

        index += 1

    return count


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_digits(text=input_text)
    print(f"Count of digits: {result}")
