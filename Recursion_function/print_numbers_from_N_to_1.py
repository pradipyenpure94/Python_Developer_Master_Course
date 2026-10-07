"""Print numbers from N to 1."""


def print_numbers(number: int) -> None:
    """Print numbers from  N to 1."""
    if number == 0:
        return
    print(number)
    print_numbers(number=number - 1)


if __name__ == "__main__":
    print_numbers(number=5)
