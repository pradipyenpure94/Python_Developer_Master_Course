"""Countdown Generator."""


def generate_countdown(limit: int):
    """Generate the countdown."""
    while limit > 0:
        yield limit
        limit -= 1


if __name__ == "__main__":
    numbers = generate_countdown(limit=5)
    print(next(numbers))
    print(next(numbers))
    print("In for loop")
    for number in numbers:
        print(number)
