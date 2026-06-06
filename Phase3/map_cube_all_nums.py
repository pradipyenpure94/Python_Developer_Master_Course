"""Cube all numbers."""


def cube_all_nums(nums: list[int]) -> list[int]:
    """
    Return the cube of all numbers.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: Cube of each number in the input list.
    """
    return list(map(lambda num: num ** 3, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = cube_all_nums(nums=numbers)
    print(f"Cube numbers list: {result}")
