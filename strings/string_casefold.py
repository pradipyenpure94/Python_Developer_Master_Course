"""Return a casefolded copy of the string.
Casefolded string may be used for caseless matching
"""

def to_casefold_string(text: str) -> str:
    """Return a casefolded copy of the string.
    Args:
        text (str): input text
    Returns:
        str: Return the lowercase string
    """
    return text.casefold()


if __name__ == "__main__":
    input_text = input("Enter a text: ")
    print(f"Result: {to_casefold_string(input_text)}")
