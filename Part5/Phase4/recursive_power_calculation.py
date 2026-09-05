"""Recursive power calculation."""


def recursive_power_calculation(base: int, exponent: int) -> int:
    """Return the power of number using recursion."""
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    if exponent == 0:
        return 1
    return base * recursive_power_calculation(base=base, exponent=exponent - 1)


if __name__ == "__main__":
    try:
        base = 2
        exponent = -1
        result = recursive_power_calculation(base=base, exponent=exponent)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result}")
