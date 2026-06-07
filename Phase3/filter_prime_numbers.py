"""Filter prime numbers."""


def is_prime(num: int) -> bool:
    """
    Check whether a number is prime or not.

    Args:
        num (int): Input number.

    Returns:
        bool: True if number is a prime, otherwise False.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def filter_prime_numbers(nums: list[int]) -> list[int]:
    """
    Return a new list containing the prime numbers.

    Args:
        nums (list[int]): Input integer numbers list.

    Returns:
        list[int]: A new list containing the prime numbers.
    """
    return list(filter(is_prime, nums))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    result = filter_prime_numbers(nums=numbers)
    print(f"Prime numbers: {result}")
