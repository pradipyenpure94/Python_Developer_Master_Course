"""Find frequency of element."""


def find_frequency_of_elements(nums: list[int]) -> dict[int, int]:
    """
    Return the frequency of each element.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        dict[int, int]: Frequency of each element.
    """
    freq = {}
    for number in nums:
        freq[number] = freq.get(number, 0) + 1
    return freq


if __name__ == "__main__":
    numbers = [1, 2, 3, 1, 4, 7, 1, 5, 9, 2, 6, 9, 2, 4, 8]
    result = find_frequency_of_elements(nums=numbers)
    print(f"Frequency of element: {result}")
