"""Prime number."""

from math import isqrt

# As per the business requirement, Defined the limits.
MIN_NUMBER = 0
MAX_NUMBER = 999999


def validate_number(number: int) -> None:
    """
    Validate the number.

    Args:
        number (int): Input number.

    Raises:
        ValueError: If the number is outside the range, it is not allowed.
    """
    if not MIN_NUMBER <= number <= MAX_NUMBER:
        raise ValueError(
            "The number must be between "
            f"{MIN_NUMBER} and {MAX_NUMBER}.")


def is_prime_number(number: int) -> bool:
    """
    Check whether the number is a prime number.

    Args:
        number (int): Input number.

    Returns:
        bool: True if the number is a prime number; otherwise, False.
    """
    if number <= 1:
        return False

    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            return False

    return True


def main() -> None:
    """Run the Program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_prime_number(number=number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
