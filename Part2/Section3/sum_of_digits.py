"""Sum of digits."""

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
            f"{MIN_NUMBER} and {MAX_NUMBER}."
        )


def sum_of_digits(number: int) -> int:
    """Return the sum of digits of the given input number."""
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10
    return total


def main() -> None:
    """Run the main program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = sum_of_digits(number=number)
        print(f"Sum of digits: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
