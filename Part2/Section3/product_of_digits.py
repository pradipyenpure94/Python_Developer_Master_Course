"""Product of digits."""

# As per the business requirement, Defined limits.
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
            f"{MIN_NUMBER} and {MAX_NUMBER}."
        )


def product_of_digits(number: int) -> int:
    """Return the product of the digits in a number."""
    temp = number
    product = 1

    if temp == 0:
        return 0

    while temp > 0:
        digit = temp % 10
        product *= digit
        temp //= 10
    return product


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
        result = product_of_digits(number=number)
        print(f"Product of digits: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
