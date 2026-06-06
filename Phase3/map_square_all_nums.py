"""Square all numbers."""


def square_all_nums(nums: list[int]) -> list[int]:
    """
    Return the square of all numbers.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: Square of each number in the input list.
    """
    return list(map(lambda num: num * num, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = square_all_nums(nums=numbers)
    print(f"Square numbers list: {result}")
