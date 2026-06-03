"""Find maximum in list."""


def find_max_nums(nums: list[int]) -> int:
    """
    Return the maximum number from list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Maximum number in list.
    """
    return max(nums)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_max_nums(nums=numbers)
    print(f"Maximum number: {result}")
