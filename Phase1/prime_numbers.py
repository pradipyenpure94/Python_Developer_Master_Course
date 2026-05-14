"""Print prime numbers from 1 to 100"""


def is_prime(num: int) -> bool:
    """check whether a number is prime or not
    Args:
        num (int): input number
    Returns:
        bool: True if number is prime, otherwise False
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_numbers = []

for number in range(1, 101):
    if is_prime(num=number):
        prime_numbers.append(number)

print(f"Prime numbers: {prime_numbers}")
