"""Power number."""


def power_of_number(base: int, exponent: int) -> int | float:
    """
    Return the power of number.

    Args:
        base (int): Input base number.
        exponent (int): Input exponent number.

    Returns:
        int | float: Power of number.
    """
    return base ** exponent


if __name__ == "__main__":
    try:
        base = int(input("Enter base number: "))
        exponent = int(input("Enter exponent number: "))
        result = power_of_number(base=base, exponent=exponent)
        print(f"Power of number is: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
