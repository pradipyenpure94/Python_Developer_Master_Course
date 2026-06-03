"""Remove duplicates from list."""


def remove_duplicate_numbers(numbers: list[int]) -> list[int]:
    """
    Return a list of unique numbers while preserving order.

    Args:
        numbers (list[int]): Input numbers list.

    Returns:
        list[int]: Unique numbers list.
    """
    seen = set()
    unique_numbers = []
    index = 0

    while index < len(numbers):
        number = numbers[index]

        if number not in seen:
            unique_numbers.append(number)
            seen.add(number)

        index += 1

    return unique_numbers


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 5, 9, 7, 5, 3, 6, 5, 4, 1, 2, 4, 8, 9]
    result = remove_duplicate_numbers(numbers=nums)
    print(f"Unique numbers List: {result}")
