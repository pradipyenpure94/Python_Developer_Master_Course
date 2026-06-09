"""Find minimum element."""

from functools import reduce


def find_min_element(nums: list[int]) -> int | None:
    """
    Return the minimum element from the list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int | None: Minimum element in the list, or None if the list is empty
    """
    if not nums:
        return None
    return reduce(lambda x, y: x if x < y else y, nums)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = find_min_element(nums=numbers)
    print(f"Minimum numbers: {result}")
