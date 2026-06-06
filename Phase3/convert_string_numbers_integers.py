"""Convert string numbers to integers."""


def convert_str_to_int_nums(words: list[str]) -> list[int]:
    """
    Return the string to integer converted list.

    Args:
        words (list[str]): Input strings of list.

    Returns:
        list[int]: Integers of list.
    """
    return list(map(lambda x: int(x), words))


if __name__ == "__main__":
    input_list = ["1", "2", "3", "4", "5"]
    result = convert_str_to_int_nums(words=input_list)
    print(f"Converted string to integer list: {result}")
