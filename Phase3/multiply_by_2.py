"""Multiply all numbers by 2."""


def multiply_by_2(nums: list[int]) -> list[int]:
    """
    Return new list containg each number multiply by 2.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list.
    """
    return list(map(lambda x: x * 2, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = multiply_by_2(nums=numbers)
    print(f"Multiply by 2 all numbers: {result}")
