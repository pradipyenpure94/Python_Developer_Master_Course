"""Recursive power function."""


def power(base: float, exponent: float) -> float:
    """
    Return the result of raising base to exponent.

    Args:
        base (float): Input base number.
        exponent (float): Input exponent number.

    Returns:
        float: Result of base raised to exponent.
    """
    if base == 0 and exponent < 0:
        raise ValueError("0 cannot be raised to a negative power.")

    # Recursive case
    if exponent < 0:
        return 1 / power(base=base, exponent=-exponent)

    # Base case: any number to the power of 0 is 1
    if exponent.is_integer():
        exponent = int(exponent)

        if exponent == 0:
            return 1
        return base * power(base=base, exponent=exponent - 1)

    # Split exponent into integer and fractional parts.
    # Example: 2.5 = 2 + 0.5
    integer_part = int(exponent)
    fractional_part = exponent - integer_part

    return power(base=base, exponent=integer_part) * (base ** fractional_part)


if __name__ == "__main__":
    try:
        base_input = float(input("Enter a base: "))
        exponent_input = float(input("Enter an exponent: "))
        result = power(base=base_input, exponent=exponent_input)
        print(f"Power of number: {result}")
    except ValueError as error:
        print(f"Error: {error}")
