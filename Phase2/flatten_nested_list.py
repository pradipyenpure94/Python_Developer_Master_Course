"""Flatten nested list."""

from typing import Any

data = [1, 2, [1, 2, 3], [4, 5, 6], [7, 8, 9, [10, 11, 12]]]


def flatten(nested_list: list[Any]) -> list[Any]:
    """Iterate sublist into single list.
    Args:
        nested_list (list[Any]): Input as sublist or int or float,..
    Returns:
        list[Any]: Flattened list
    """
    flat = []

    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


print(f"Flattened List: {flatten(nested_list=data)}")
