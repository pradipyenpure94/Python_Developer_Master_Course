"""Remove spaces using map."""


def remove_spaces(words: list[str]) -> list[str]:
    """
    Remove spaces from list elements.

    Args:
        words (list[str]): Input words list.

    Returns:
        list[str]: A new list with removed leading and trailing whitespace
        from each string in the list.
    """
    return list(map(str.strip, words))


if __name__ == "__main__":
    words = [" ", " 20LPA", " Python"]
    result = remove_spaces(words=words)
    print(f"Remove spaces: {result}")
