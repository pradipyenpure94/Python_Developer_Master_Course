"""Find smallest number."""


def find_smallest_number(nums: list[int]) -> int:
    """Return the second smallest number from list.
    Args:
        nums (list[int]): Input numbers list.
    Returns:
        int: Second smallest number from list.
    Raises:
        ValueError: If the list doesnot contain at least two distinct numbers.
    """
    if len(set(nums)) < 2:
        raise ValueError("Need at least two distinct numbers \
            to find second smallest number.")

    smallest_number = second_smallest_number = float('inf')

    for number in nums:
        if number < smallest_number:
            second_smallest_number = smallest_number
            smallest_number = number

        elif number < second_smallest_number:
            second_smallest_number = number

    return second_smallest_number


if __name__ == "__main__":
    numbers = [1, 2, 3, 5, 2, 4, 8, 9, 7]
    result = find_smallest_number(nums=numbers)
    print(f"Second smallest number: {result}")
