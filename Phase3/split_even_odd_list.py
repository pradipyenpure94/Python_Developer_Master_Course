"""Split even and odd lists."""


def split_even_odd_lists(nums: list[int]) -> tuple[list[int], list[int]]:
    """
    Return the even and odd lists.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        tuple[list[int], list[int]]: A tuple contain even and odd lists.
    """
    even_nums = [num for num in nums if num % 2 == 0]
    odd_nums = [num for num in nums if num % 2 == 1]
    return even_nums, odd_nums


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even, odd = split_even_odd_lists(nums=numbers)
    print(f"Even numbers: {even}")
    print(f"Odd numbers: {odd}")
