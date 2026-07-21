"""LCM."""

from math import lcm
from get_gcd import validate_number


def calculate_lcm(first_number: int, second_number: int) -> int:
    """
    Return the LCM of two input numbers.

    Args:
        first_number (int): First input number.
        second_number (int): Second input number.

    Returns:
        int: The least common multiple of two input numbers.
    """
    return lcm(first_number, second_number)


def main() -> None:
    """Run the Main Program."""
    try:
        first_number = int(input("Enter the first number: "))
        validate_number(number=first_number, field_name="First number")
        second_number = int(input("Enter the second number: "))
        validate_number(number=second_number, field_name="Second number")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = calculate_lcm(
            first_number=first_number,
            second_number=second_number
        )
        print(f"LCM: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
