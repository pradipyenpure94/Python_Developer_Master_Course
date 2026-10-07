"""Print numbers from 1 to N."""


def print_numbers(number: int) -> None:
    """Print numbers from 1 to N."""
    if number <= 0:
        return
    print_numbers(number=number - 1)
    print(number)


if __name__ == "__main__":
    print_numbers(number=5)
