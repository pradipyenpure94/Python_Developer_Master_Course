"""Filter empty strings."""


def filter_empty_strings(words: list[str]) -> list[str]:
    """
    Return a new list with all empty strings removed.
    Args:
        words (list[str]): Input words list.
    Returns:
        list[str]: A new list containing only non-empty strings.
    """
    return list(filter(None, words))


if __name__ == "__main__":
    input_words = ["", "amit", "pradip", "", "akshay"]
    result = filter_empty_strings(words=input_words)
    print(f"Filter empty strings: {result}")
