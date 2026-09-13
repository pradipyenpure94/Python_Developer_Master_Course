"""Square Number Generator."""


from collections.abc import Generator


def generate_square_number(limit: int) -> Generator[int]:
    """Generate the square numbers."""
    for number in range(limit):
        yield number ** 2


if __name__ == "__main__":
    square_numbers = generate_square_number(limit=5)
    print(next(square_numbers))
    print(next(square_numbers))
    print(next(square_numbers))
    print("In for loop")
    for number in square_numbers:
        print(number)
