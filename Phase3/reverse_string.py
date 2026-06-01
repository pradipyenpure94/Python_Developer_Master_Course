"""Reverse string."""


def reverse_string(text: str) -> str:
    """
    Return the reverse string.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed string.
    """
    return text[::-1]


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = reverse_string(text=input_text)
    print(f"Reversed string: {result}")
