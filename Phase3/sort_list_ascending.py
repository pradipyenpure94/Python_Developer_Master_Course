"""Sort list ascending."""


def sort_list_ascending_order(nums: list[int]) -> list[int]:
    """
    Return a list sorted in ascending order using sort().

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: Sorted list in ascending order.
    """
    nums = nums[:]
    nums.sort()
    return nums


if __name__ == "__main__":
    numbers = [1, 5, 9, 7, 5, 3, 4, 5, 6, 9, 7, 2]
    result = sort_list_ascending_order(nums=numbers)
    print(f"Sorted list in ascending order: {result}")
