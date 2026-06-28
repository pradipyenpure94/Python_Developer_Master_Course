"""Find first non repeating character."""

from count_frequency_each_char import count_character_frequency


def find_first_non_repeating_char(text: str) -> str | None:
    """
    Return the first non-repeating character in the input text.

    Args:
        text (str): Input text.

    Returns:
        str | None: The first non-repeating character, or None
        if no such character exist.
    """
    freq = count_character_frequency(text=text)
    for key, value in freq.items():
        if value == 1:
            return key
    return None


if __name__ == "__main__":
    try:
        input_text = input("Enter a string: ")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        result = find_first_non_repeating_char(text=input_text)
        print(f"First non-repeating character: {result}")
    finally:
        print("Operation completed.")
