"""Generate Numbers Greater Than a Given Value."""


from collections.abc import Generator


def generate_numbers(numbers: list[int], value: int) -> Generator:
    """Generate the numbers."""
    for number in numbers:
        if number > value:
            yield number


if __name__ == "__main__":
    numbers = [10, 50, 20, 70, 30, 90]
    threshold = 50

    filtered_numbers = generate_numbers(numbers=numbers, value=threshold)
    print(next(filtered_numbers))
    print(next(filtered_numbers))
