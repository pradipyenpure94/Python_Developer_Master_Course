"""Recursive reverse string."""


def recursive_reverse_string(text: str) -> str:
    """
    Return the reversed string.

    Args:
        text (str): Input string.

    Returns:
        str: The input string in reverse order.
    """
    if len(text) <= 1:
        return text
    return recursive_reverse_string(text[1:]) + text[0]


if __name__ == "__main__":
    input_text = input("Enter a text: ")
    result = recursive_reverse_string(text=input_text)
    print(f"Reversed string: {result}")
