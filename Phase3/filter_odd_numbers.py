"""Filter odd numbers."""


def filter_odd_numbers(nums: list[int]) -> list[int]:
    """
    Return the odd number list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list of odd numbers.
    """
    return list(filter(lambda num: num % 2 == 1, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_odd_numbers(nums=numbers)
    print(f"Odd numbers: {result}")
