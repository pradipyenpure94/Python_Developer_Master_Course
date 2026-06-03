"""Count odd numbers in list."""


def count_odd_numbers(nums: list[int]) -> int:
    """
    Return the number of odd integers in list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: Number of odd integers in the list.
    """
    count = 0

    for number in nums:
        if number % 2 == 1:
            count += 1
    return count


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    result = count_odd_numbers(nums=numbers)
    print(f"Count of odd numbers: {result}")
