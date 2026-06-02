"""Count special characters."""


def count_special_characters(text: str) -> int:
    """
    Return the special characters count in string.

    Args:
        text (str): Input text.

    Returns:
        int: Count of special characters in string.
    """
    count = 0
    index = 0

    while index < len(text):
        char = text[index]
        if not char.isalnum() and not char.isspace():
            count += 1

        index += 1

    return count


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_special_characters(text=input_text)
    print(f"Count of special characters: {result}")
