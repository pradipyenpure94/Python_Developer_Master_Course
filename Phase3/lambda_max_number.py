"""Lambda for maximum number."""


def find_max_number(nums: list[int]) -> int:
    """
    Return the maximum number.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Maximum number.
    """
    if not nums:
        raise ValueError("List cannot be empty.")
    max_number = lambda numbers: max(numbers)
    return max_number(nums)


if __name__ == "__main__":
    numbers = [10, 20, 30, 10]
    result = find_max_number(nums=numbers)
    print(f"Max. number: {result}")
