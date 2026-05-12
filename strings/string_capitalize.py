"""Return the first character capitalized and the rest lowercased"""

def to_capitalize(text: str) -> str:
    """Return the first character capitalized and rest lowercased
    Args:
        text (str): input text
    Returns:
        str: first character capitalized and rest lowercased
    """
    return text.capitalize()

if __name__ == "__main__":
    input_text = input("Enter a text: ")
    print(f"Result: {to_capitalize(input_text)}")
