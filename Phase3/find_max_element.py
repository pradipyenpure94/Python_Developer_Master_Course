"""Find maximum element."""

from functools import reduce


def find_maximum_element(nums: list[int]) -> int | None:
    """
    Return the maximum element from the list.

    Args:
        nums (list[int]): Input element list.

    Returns:
        int | None: Maximum element in the list, or None if the list is empty.
    """
    if not nums:
        return None
    return reduce(max, nums)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers = []
    result = find_maximum_element(nums=numbers)
    print(f"Maximum element: {result}")
