"""Remove duplicates from list."""


def remove_duplicate_numbers(numbers: list[int]) -> list[int]:
    """
    Return a list of unique numbers while preserving order.

    Args:
        numbers (list[int]): Input numbers list.

    Returns:
        list[int]: Unique numbers list.
    """
    unique_nums = []
    seen = set()

    for num in numbers:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)
    return unique_nums


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 5, 9, 7, 5, 3, 6, 5, 4, 1, 2, 4, 8, 9]
    result = remove_duplicate_numbers(numbers=nums)
    print(f"Unique numbers List: {result}")
