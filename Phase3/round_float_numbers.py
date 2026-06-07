"""Round float numbers."""


def round_float_numbers(nums: list[float]) -> list[int]:
    """
    Return a new list containing round values.

    Args:
        nums (list[float]): Input numbers list.

    Returns:
        list[int]: A new list containing the rounded values.
    """
    return list(map(round, nums))


if __name__ == "__main__":
    numbers = [3.14, 9.8, 1.4]
    result = round_float_numbers(nums=numbers)
    print(f"Result: {result}")
