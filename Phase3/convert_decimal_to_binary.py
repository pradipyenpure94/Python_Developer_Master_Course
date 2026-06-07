"""Convert decimal to binary."""


def convert_decimal_to_binary(nums: list[int]) -> list[str]:
    """
    Return a new list containing the binary representation of each number.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[str]: A new list containing the binary representation of each
        number.
    """
    return list(map(bin, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = convert_decimal_to_binary(nums=numbers)
    print(f"Convert decimal to binary: {result}")
