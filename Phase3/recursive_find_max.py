"""Find largest element using recursive."""


def find_largest_num(nums: list[int]) -> int:
    """
    Return the largest number from the list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Largest number in the list.
    """
    if not nums:
        raise ValueError("List cannot be empty.")

    if len(nums) == 1:
        return nums[0]
    max_of_rest = find_largest_num(nums=nums[1:])
    return nums[0] if nums[0] > max_of_rest else max_of_rest


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_largest_num(nums=numbers)
    print(f"Largest number: {result}")
