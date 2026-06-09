"""Filter duplicate values."""


def filter_duplicate_values(nums: list[int]) -> list[int]:
    """
    Return a new list containing unique values while preserving order.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing unique values.
    """
    seen = set()
    return list(filter(lambda num: num not in seen and not seen.add(num),
                       nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 1, 5, 6, 2, 4, 3, 6, 9, 7, 8, 5, 6, 4, 9]
    result = filter_duplicate_values(nums=numbers)
    print(f"Filter duplicate values: {result}")
