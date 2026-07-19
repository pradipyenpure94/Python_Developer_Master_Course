"""Check strong number."""

# As per the business requirement, Defined the limits.
MIN_NUMBER = 0
MAX_NUMBER = 9999

FACTORIAL_NUMBERS = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880
}


def validate_number(number: int) -> None:
    """
    Validate the number.

    Args:
        number: Input number.

    Raises:
        ValueError: If the number is outside the range, it is not allowed.
    """
    if not MIN_NUMBER <= number <= MAX_NUMBER:
        raise ValueError(
            "The number must be between "
            f"{MIN_NUMBER} and {MAX_NUMBER}.")


def is_strong_number(number: int) -> bool:
    """
    Check whether the number is a strong number.

    Args:
        number (int): Input number.

    Returns:
        bool: True, if the number is a strong number; otherwise, False.
    """
    temp = number

    if temp == 0:
        return False

    total = 0

    while temp > 0:
        digit = temp % 10
        total += FACTORIAL_NUMBERS[digit]
        temp //= 10

    return number == total


def main() -> None:
    """Run the Program"""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_strong_number(number=number):
            print(f"{number} is a strong number.")
        else:
            print(f"{number} is not a strong number.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
