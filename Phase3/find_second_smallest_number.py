"""Find second smallest number."""


def find_second_smallest_number(nums: list[int]) -> int:
    """Return the second smallest number from list.
    Args:
        nums (list[int]): Input numbers list.
    Returns:
        int: Second smallest number from list.
    Raises:
        ValueError: If the list does not contain at least two distinct numbers.
    """
    if len(set(nums)) < 2:
        raise ValueError("Need at least two distinct numbers to find second smallest number.")

    smallest_number = second_smallest_number = float('inf')
    index = 0

    while index < len(nums):
        number = nums[index]

        if number < smallest_number:
            second_smallest_number = smallest_number
            smallest_number = number

        elif number < second_smallest_number:
            second_smallest_number = number

        index += 1

    return second_smallest_number


if __name__ == "__main__":
    numbers = [1, 2, 3, 5, 2, 4, 8, 9, 7]
    result = find_second_smallest_number(nums=numbers)
    print(f"Second smallest number: {result}")
