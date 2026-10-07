"""Sum of first N natural numbers."""


def sum_of_natural_numbers(number: int) -> int:
    """Return the sum of first N natural numbers."""
    if number == 0:
        return 0
    return number + sum_of_natural_numbers(number=number - 1)


if __name__ == "__main__":
    result = sum_of_natural_numbers(number=10)
    print(f"Result: {result}")
