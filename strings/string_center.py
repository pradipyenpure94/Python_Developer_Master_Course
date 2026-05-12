"""Return centered string with specified width and fill character."""

def to_center_string(text: str, width: int, fill_char: str) -> str:
    """Return centered string with given width
    Args:
        text (str): input text
        width (int): a string of length of width
        fill_char (str): character, ex.,'@','*','-',etc
    Returns:
        str: centered string
    """
    return text.center(width, fill_char)

if __name__ == "__main__":
    input_text = input("Enter a text: ")
    try:
        input_width = int(input("Enter width: "))
        input_fill_char = input("Enter a fill character: ").strip()
        print(f"Result: {to_center_string(text=input_text, width=input_width,
                                            fill_char=input_fill_char)}")
    except (ValueError, TypeError) as e:
        print(e)
