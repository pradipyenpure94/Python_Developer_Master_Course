"""GCD."""

from math import gcd

# As per the business requirement, Defined the limits.
MIN_NUMBER = 1
MAX_NUMBER = 9999


def validate_number(number: int, field_name: str) -> None:
    """
    Validate the number.

    Raises:
        ValueError: If the number is outside range. its not allowed.
    """
    if not MIN_NUMBER <= number <= MAX_NUMBER:
        raise ValueError(
            f"The {field_name} must be between {MIN_NUMBER} and {MAX_NUMBER}."
        )


def calculate_gcd(first_number: int, second_number: int) -> int:
    """
    Return a GCD number.

    Args:
        first_number (int): First input number.
        second_number (int): Second input number.

    Returns:
        int: GCD number.
    """
    return gcd(first_number, second_number)


def main() -> None:
    """Run the Program."""
    try:
        first_number = int(input("Enter the first number: "))
        validate_number(number=first_number, field_name="first number")
        second_number = int(input("Enter the second number: "))
        validate_number(number=second_number, field_name="second number")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = calculate_gcd(
            first_number=first_number,
            second_number=second_number
        )
        print(f"GCD: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
