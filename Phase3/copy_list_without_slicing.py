"""Copy list without slicing."""


def copy_list(nums: list[int]) -> list[int]:
    """
    Return a copy of the input list.

    Args:
        nums (list[int]): Original list.

    Returns:
        list[int]: A shallow copy of the input list.
    """
    return nums.copy()


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = copy_list(nums=numbers)
    print(f"Duplicate copy of list: {result}")
