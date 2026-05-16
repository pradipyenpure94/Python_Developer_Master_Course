"""Find the prime numbers from list."""


def is_prime(number: int) -> bool:
    """check whether a number is prime
    Args:
        number (int): input integer number
    Returns:
        bool: True if number is prime otherwise False
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = []
index = 0
length = len(numbers)

while index < length:
    current_number = numbers[index]
    if is_prime(number=current_number):
        prime_numbers.append(current_number)
    index += 1

print(f"Prime numbers: {prime_numbers}")
