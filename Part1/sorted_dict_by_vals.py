"""Sort dictionary by values."""


def sort_dict_by_vals(data: dict[str, int]) -> dict[str, int]:
    """
    Return a new dictionary sorted by its values.

    Args:
        data (dict[str, int]): Input data dictionary.

    Returns:
        dict[str, int]: A new sorted dictionary by its values.
    """
    return dict(sorted(data.items(), key=lambda item: item[1]))


if __name__ == "__main__":
    fruits = {'Mango': 2, 'Orange': 2, 'Banana': 1}
    print(f"Fruits: {fruits}")
    result = sort_dict_by_vals(data=fruits)
    print(f"Sorted dictionary values: {result}")
