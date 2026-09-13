"""Generate for squares."""


def generate_square_number(limit):
    """Generate square numbers."""
    for number in range(1, limit + 1):
        yield number ** 2


for number in generate_square_number(5):
    print(number)
