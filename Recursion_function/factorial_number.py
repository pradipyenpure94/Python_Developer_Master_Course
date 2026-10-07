"""Calculate the factorial number."""


def factorial_number(number: int) -> int:
    """Return the number of factorial."""

    if number == 0 or number == 1:
        return 1
    return number * factorial_number(number=number - 1)


if __name__ == "__main__":
    result = factorial_number(number=5)
    print(f"Result: {result}")
