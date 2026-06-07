"""Find absolute values."""


def find_absolute_values(nums: list[float | int]) -> list[float | int]:
    """
    Return a new list containing the absolute value of each number.

    Args:
        nums (list[float | int]): Input numbers list.

    Returns:
        list[float | int]: A new list containing absolute values.
    """
    return list(map(abs, nums))


if __name__ == "__main__":
    numbers = [-1, 1.2, -3.5, 4.5, -3.14]
    result = find_absolute_values(nums=numbers)
    print(f"Absolute values: {result}")
