"""Remove duplicate character."""


def remove_duplicate_chars(text: str) -> str:
    """
    Remove the duplicate characters from the input string.

    Args:
        text (str): Input text.

    Returns:
        str: String containing the first occurrence of each character.
    """
    unique_chars = []
    seen = set()
    for char in text:
        if char not in seen:
            unique_chars.append(char)
            seen.add(char)
    return "".join(unique_chars)


if __name__ == "__main__":
    try:
        input_text = input("Enter a string: ").strip()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = remove_duplicate_chars(text=input_text)
        print(f"Unique characters: {result}")
    finally:
        print("Operation completed.")
