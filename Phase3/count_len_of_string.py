"""Count length of string without using len()"""


def count_string_length(text: str) -> int:
    """
    Return the length of string.

    Args:
        text (str): Input text.

    Returns:
        int: length of input string.
    """
    count = 0
    try:
        while True:
            text[count]
            count += 1
    except IndexError:
        return count


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = count_string_length(text=input_text)
    print(f"Length of string: {result}")
