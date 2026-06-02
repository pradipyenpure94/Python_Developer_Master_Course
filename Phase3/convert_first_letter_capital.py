"""Convert first letter capital."""


def to_capitalize(text: str) -> str:
    """
    Return the first letter capital and rest are lowercase.
    Args:
        text (str): Input text.
    Returns:
        str: First letter capital and rest are lowercased.
    """
    return text.capitalize()


if __name__ == "__main__":
    input_text = input("Enter a string: ")
    result = to_capitalize(text=input_text)
    print(f"Titale case: {result}")
