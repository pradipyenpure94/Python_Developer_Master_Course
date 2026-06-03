"""Find minimum in list."""


def find_minimum_number(nums: list[int]) -> int:
    """
    Return the minimum number from list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Minimum number from list.

    Raises:
        ValueError: If list is empty.
    """
    if not nums:
        raise ValueError("List cannot be empty.")

    min_num = nums[0]

    for number in nums[1:]:
        if number < min_num:
            min_num = number

    return min_num


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_minimum_number(nums=numbers)
    print(f"Minimum number: {result}")
