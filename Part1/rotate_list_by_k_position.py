"""Rotate list by k position."""

from typing import TypeVar
T = TypeVar("T")


def rotate_list(data: list[T], position: int = 2) -> list[T]:
    """
    Return a new list rotated to the left by the given number of positions.

    Args:
        data (list[T]): Input data list.
        position (int): A number of positions to rotate the list to the left.
                        Defaults to 2.

    Returns:
        list[T]: A new list rotated to the left by the
        specified number of positions.
    """
    return data[position:] + data[:position]


if __name__ == "__main__":
    input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Input data: {input_data}")
    result = rotate_list(data=input_data, position=3)
    print(f"After rotation: {result}")
