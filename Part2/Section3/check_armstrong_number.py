"""Armstrong number."""

from count_digits import count_digits

# As per the business requirement, defined limits.
MIN_NUMBER = 0
MAX_NUMBER = 99999


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


def is_armstrong_number(number: int) -> bool:
    """
    Check whether the given number is an Armstrong number.

    Args:
        number (int): Input number.

    Returns:
        bool: True if the number is an Armstrong number; otherwise, False.
    """
    # Count digits
    digits_count = count_digits(number=number)
    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits_count
        temp //= 10
    return number == total


def main() -> None:
    """Run the Program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("Operation cancelled by the user.")
    else:
        if is_armstrong_number(number=number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
