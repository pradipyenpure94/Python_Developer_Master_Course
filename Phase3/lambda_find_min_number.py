"""Lambda for minimum number."""


def find_min_number(nums: list[int]) -> int:
    """
    Return the minimum number.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Minimum number.
    """
    if not nums:
        raise ValueError("List cannot be empty.")
    min_number = lambda numbers: min(numbers)
    return min_number(nums)


if __name__ == "__main__":
    numbers = [1, 2, 3, 1, 5, 6, 7, 5, 3]
    result = find_min_number(nums=numbers)
    print(f"Minimum number: {result}")
