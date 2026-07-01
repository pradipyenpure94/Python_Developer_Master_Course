"""Filter even numbers using filter()."""


def filter_even_numbers(nums: list[int]) -> list[int]:
    """
    Return a new list containing only even numbers.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing only even numbers.
    """
    return list(filter(lambda x: x % 2 == 0, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Numbers: {numbers}")
    result = filter_even_numbers(nums=numbers)
    print(f"Filtered even numbers: {result}")
