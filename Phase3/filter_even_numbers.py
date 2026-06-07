"""Filter even numbers."""


def filter_even_numbers(nums: list[int]) -> list[int]:
    """
    Return the even numbers list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing the even numbers.
    """
    return list(filter(lambda num: num % 2 == 0, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even_numbers(nums=numbers)
    print(f"Even numbers: {result}")
