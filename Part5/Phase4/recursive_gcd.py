"""Recursive GCD."""


def recursive_gcd(first_number: int, second_number: int) -> int:
    """Return the GCD of number."""

    return first_number if second_number == 0 else recursive_gcd(
        first_number=second_number,
        second_number=first_number % second_number
    )


if __name__ == "__main__":
    first_number = 48
    second_number = 18

    result = recursive_gcd(
        first_number=first_number,
        second_number=second_number
    )
    print(f"GCD: {result}")
