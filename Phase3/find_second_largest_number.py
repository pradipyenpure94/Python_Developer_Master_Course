"""Find second largest number."""


def find_second_largest_number(nums: list[int]) -> int:
    """
    Return the second largest number from list

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Second largest number from list.

    Raises:
        ValueError: If the list does not contain at least two distinct numbers.
    """
    if len(set(nums)) < 2:
        raise ValueError(
            "Need at least two distinct numbers to find second largest.")

    largest_num = second_largest_num = float('-inf')
    index = 0

    while index < len(nums):
        number = nums[index]
        if number > largest_num:
            second_largest_num = largest_num
            largest_num = number

        elif number > second_largest_num:
            second_largest_num = number

        index += 1

    return second_largest_num


if __name__ == "__main__":
    numbers = [4, 1, 5, 10, 1]
    result = find_second_largest_number(nums=numbers)
    print(f"Second Largest number: {result}")
