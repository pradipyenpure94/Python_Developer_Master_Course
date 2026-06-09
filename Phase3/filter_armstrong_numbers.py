"""Filter Armstrong numbers."""


def power_of_number(num: int) -> int:
    """
    Return the number of digits in a number.

    Args:
        num (int): Input number.

    Returns:
        int: Number of digits in the input number.
    """
    temp = num
    count = 0

    if temp == 0:
        return 1

    while temp > 0:
        count += 1
        temp //= 10
    return count


def is_armstrong(num: int) -> bool:
    """
    Check whether a number is an Armstrong number.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is an Armstrong number, otherwise False.
    """
    if num < 0:
        return False

    if num == 0:
        return True

    power = power_of_number(num=num)
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10
    return total == num


def filter_armstrong_numbers(nums: list[int]) -> list[int]:
    """
    Return a new list containing Armstrong numbers.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing Armstrong numbers.
    """
    return list(filter(is_armstrong, nums))


if __name__ == "__main__":
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 144, 145]
    result = filter_armstrong_numbers(nums=numbers)
    print(f"Filter armstrong numbers: {result}")
