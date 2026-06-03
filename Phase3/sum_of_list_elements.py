"""Find sum of list elements."""


def sum_of_list_numbers(nums: list[int]) -> int:
    """
    Return the sum of list elements.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        int: sum of list elements.
    """
    total = 0

    for number in nums:
        total += number
    return total


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sum_of_list_numbers(nums=numbers)
    print(f"Sum of List elements: {result}")
