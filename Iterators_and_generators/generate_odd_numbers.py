"""Generate odd numbers."""


def odd_numbers(limit):
    """Generate odd numbers."""
    for number in range(1, limit + 1, 2):
        yield number


for number in odd_numbers(10):
    print(number)
