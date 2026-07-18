"""Count digits."""

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


def count_digits(number: int) -> int:
    """Return the count of the digits in a number."""
    count = 0
    temp = number

    if temp == 0:
        return 1

    while temp > 0:
        count += 1
        temp //= 10
    return count


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
        result = count_digits(number=number)
        print(f"Count of digits: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
