"""Find ASCII value."""


def find_ascii_value(char: str) -> int:
    """
    Return the ASCII value of a character.

    Args:
        char (str): Input single character.

    Returns:
        int: ASCII value of character.
    """
    if len(char) != 1:
        raise ValueError("Invalid input! Please enter single character only.")
    return ord(char)


if __name__ == "__main__":
    character = input("Enter charcter: ")
    result = find_ascii_value(char=character)
    print(f"ASCII value of {character} is: {result}")
