"""Find square using lambda."""


def find_square(nums: list[int]) -> list[int]:
    """
    Return a list containing the square of each number.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A list containing the square of each input number.
    """
    return list(map(lambda x: x*x, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(f"Input numbers: {numbers}")
    result = find_square(nums=numbers)
    print(f"Square numbers: {result}")
