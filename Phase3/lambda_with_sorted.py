"""Lambda with sorted()."""


def sorted_numbers(nums: list[int]) -> list[int]:
    """
    Return the sorted list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: Sorted list.
    """
    return sorted(nums, key=lambda x: x)


if __name__ == "__main__":
    numbers = [1, 5, 9, 7, 5, 3, 4, 5, 6]
    result = sorted_numbers(nums=numbers)
    print(f"Sorted numbers: {result}")
