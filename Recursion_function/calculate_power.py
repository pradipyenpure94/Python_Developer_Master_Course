"""Calculate the power of number."""


def power(base: int, exponent: int) -> int:
    """Return base raised to the given exponent."""
    if exponent == 0:
        return 1
    return base * power(base=base, exponent=exponent - 1)


if __name__ == "__main__":
    result = power(base=5, exponent=3)
    print(f"Result: {result}")
