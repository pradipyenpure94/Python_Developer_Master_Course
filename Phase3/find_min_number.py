"""Find minimum number."""


def find_min_number(*numbers: int) -> int:
    """Return the smallest value from the given input numbers.

    Args:
        *numbers (int): Input numbers.

    Returns:
        int: Minimum number of input numbers.
    """
    return min(numbers)


if __name__ == "__main__":
    try:
        minimum_number = find_min_number(10, 20, 30)
        print(f"Minimum number: {minimum_number}")
    except ValueError as error:
        print(error)
