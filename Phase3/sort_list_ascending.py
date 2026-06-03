"""Sort list ascending."""


def sort_list_ascending_order(nums: list[int]) -> list[int]:
    """
    Sort list ascending order.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: Sorted list in ascending order.
    """
    # Implement bubble sort with early exit optimization
    n = len(nums)
    nums = nums[:]

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break
    return nums


if __name__ == "__main__":
    numbers = [1, 5, 9, 7, 5, 3, 4, 5, 6, 9, 7, 2]
    result = sort_list_ascending_order(nums=numbers)
    print(f"Sorted list in ascending order: {result}")
