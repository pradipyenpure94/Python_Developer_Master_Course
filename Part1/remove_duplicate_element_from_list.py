"""Remove duplicate elements from a list."""

from typing import TypeVar


T = TypeVar("T")


def unique_elements(data: list[T]) -> list[T]:
    """
    Return the unique elements in a input list.

    Args:
        data (list[T]): Input list.

    Returns:
        list[T]: A list containing the unique elements.
    """
    unique_items = []
    seen = set()

    for item in data:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)

    return unique_items


if __name__ == "__main__":
    input_data = ["Pradip", "amit", "sandeep", "Pradip", "amit"]
    print(f"Input data: {input_data}")
    result = unique_elements(data=input_data)
    print(f"Unique input data: {result}")
