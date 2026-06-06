"""Add 10 to all list elements."""


def add_10_to_all_list_elements(nums: list[int]) -> list[int]:
    """
    Return new list containing each element to add 10.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: New list.
    """
    return list(map(lambda x: x + 10, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = add_10_to_all_list_elements(nums=numbers)
    print(f"Add 10 to all list elements: {result}")
