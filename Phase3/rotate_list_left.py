"""Rotate list left."""


def rotate_list_left(numbers: list[int], shift_position: int = 2) -> list[int]:
    """
    Return the rotate left position.

    Args:
        numbers (list[int]): Input numbers list.
        shift_position: Rotate by k position

    Returns:
        list[int]: A new list.
    """
    if not numbers:
        return []

    k = shift_position % len(numbers)
    return numbers[k:] + numbers[:k]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = rotate_list_left(numbers=nums)
    print(f"Rotate by left position: {result}")
