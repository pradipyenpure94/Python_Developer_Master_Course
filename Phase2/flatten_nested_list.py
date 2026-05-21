"""Flatten nested list."""

from typing import Any

data = [1, 2, [1, 2, 3], [4, 5, 6], [7, 8, 9, [10, 11, 12]]]


def flatten(nested_list: list[Any]) -> list[Any]:
    """Flatten nested lists into a single list.
    Args:
        nested_list (list[Any]): Input nested list containing lists or values.
    Returns:
        list[Any]: Flattened list
    """
    flat = []
    index = 0

    while index < len(nested_list):
        current_item = nested_list[index]
        if isinstance(current_item, list):
            flat.extend(flatten(current_item))
        else:
            flat.append(current_item)

        index += 1

    return flat


print(f"Flattened List: {flatten(nested_list=data)}")
