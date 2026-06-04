"""Rotate list right"""


def rotate_list_right(numbers: list[int], position: int = 2) -> list[int]:
    """
    Return the rotate list by k position.

    Args:
        numbers list[int]: Input numbers list.
        position (int): Rotate list by k position.

    Returns:
        list[int]: A new list.
    """
    if not numbers:
        return []
    k = position % len(numbers)
    return numbers[-k:] + numbers[:-k]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = rotate_list_right(numbers=nums)
    print(f"Rotate list right position: {result}")
