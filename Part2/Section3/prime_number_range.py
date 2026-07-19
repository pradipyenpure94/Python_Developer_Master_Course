"""Prime numbers in range."""

from check_prime_number import is_prime_number

# As per the business requirement, Defined the limits.
MIN_NUMBER = 0
MAX_NUMBER = 9999


def validate_numbers_range(
    number: int,
    minimum: int,
    maximum: int,
    field_name: str
) -> None:
    """
    Validate the numbers range.

    Args:
        number (int): Input number.
        minimum (int): Minimum input number limit.
        maximum (int): Maximum input number limit.
        field_name (str): The field name.

    Raises:
        ValueError: If the start and end input numbers are outside the range,
                    it is not allowed.
    """
    if not minimum <= number <= maximum:
        raise ValueError(
            f"The {field_name} number must be between "
            f"{minimum} and {maximum}.")


def validate_range(start: int, end: int) -> None:
    """Validate the input range, i.e., the start and end input numbers."""
    if not start <= end:
        raise ValueError(
            "The start number cannot be greater than the end number."
        )


def get_prime_numbers(start: int, end: int) -> list[int]:
    """
    Return the prime numbers list.

    Args:
        start (int): Input start number.
        end (int): Input end number.

    Returns:
        list[int]: Prime numbers list.
    """
    prime_numbers = []

    for number in range(start, end + 1):
        if is_prime_number(number=number):
            prime_numbers.append(number)

    return prime_numbers


def main() -> None:
    """Run the Program."""
    try:
        start = int(input("Enter the start number: "))
        validate_numbers_range(
            number=start,
            minimum=MIN_NUMBER,
            maximum=MAX_NUMBER,
            field_name="start"
        )

        end = int(input("Enter the end number: "))
        validate_numbers_range(
            number=end,
            minimum=MIN_NUMBER,
            maximum=MAX_NUMBER,
            field_name="end"
        )

        validate_range(start=start, end=end)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = get_prime_numbers(start=start, end=end)
        print(f"Prime numbers are: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
