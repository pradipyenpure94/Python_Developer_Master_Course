"""Convert list into string list."""


def convert_list_into_string_list(nums: list[int]) -> list[str]:
    """
    Return a new list with all items converted to string

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[str]: A new list containing the string representation
                of each item.
    """
    return list(map(str, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = convert_list_into_string_list(nums=numbers)
    print(f"Convert list into string of list: {result}")
