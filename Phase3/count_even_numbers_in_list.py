"""Count even numbers in list."""


def count_even_numbers(nums: list[int]) -> int:
    """
    Return the count of even numbers in list

    Args:
        nums (list[int]): Input numbers list

    Returns:
        int: Count of even numbers list.
    """
    count = 0

    for number in nums:
        if number % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = count_even_numbers(nums=numbers)
    print(f"Count even numbers: {result}")
