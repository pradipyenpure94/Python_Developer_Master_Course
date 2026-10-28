"""Print all prime numbers within a given range."""

start_number = 1
end_number = 100


def is_prime_number(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for number in range(start_number, end_number + 1):
    if is_prime_number(number=number):
        print(number)
