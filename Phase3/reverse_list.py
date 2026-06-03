"""Reverse List."""


def reverse_list(nums: list[int]) -> list[int]:
    """Return the reverse list.
    Args:
        nums (list[int]): Input numbers list.
    Returns:
        list[int]: Reversed list.
    """
    return nums[::-1]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = reverse_list(nums=numbers)
    print(f"Reversed List: {result}")
