"""Filter negative numbers."""


def filter_negative_numbers(nums: list[int | float]) -> list[int | float]:
    """
    Return the negative numbers list.

    Args:
        nums (list[int | float]): Input numbers list.

    Returns:
        list[int | float]: A new list containing the negative numbers.
    """
    return list(filter(lambda num: num < 0, nums))


if __name__ == "__main__":
    numbers = [-1, 2, -2.5, 3.2, 8, -9.5]
    result = filter_negative_numbers(nums=numbers)
    print(f"Negative numbers: {result}")
