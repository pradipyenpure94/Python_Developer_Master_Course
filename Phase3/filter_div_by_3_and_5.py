"""Filter divisible by 3 and 5."""


def filter_div_by_3_and_5(nums: list[int]) -> list[int]:
    """
    Return a new list containing numbers divisible by 3 and 5.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing numbers divisible by 3 and 5.
    """
    return list(filter(lambda num: num % 3 == 0 and num % 5 == 0, nums))


if __name__ == "__main__":
    numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    result = filter_div_by_3_and_5(nums=numbers)
    print(f"Filter numbers: {result}")
