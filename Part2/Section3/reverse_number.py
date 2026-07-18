"""Reverse number."""

# As per the business requirement, defined the terms.
MIN_NUMBER = 0
MAX_NUMBER = 99999


def validate_number(number: int) -> None:
    """
    Validate the number.

    Args:
        number (int): Input number.

    Raises:
        ValueError:
            If the input number is outside the allowed range.
    """
    if not MIN_NUMBER <= number <= MAX_NUMBER:
        raise ValueError(
            "The number should be between "
            f"{MIN_NUMBER} and {MAX_NUMBER}."
        )


def reverse_number(number: int) -> int:
    """
    Return a reverse number.

    Args:
        number (int): Input number from user.
    Returns:
        int: Return the reversed number.
    """
    temp = number
    reversed_number = 0

    if number == 0:
        return 0

    while temp > 0:
        digit = temp % 10
        reversed_number = reversed_number * 10 + digit
        temp //= 10
    return reversed_number


def main() -> None:
    """Run the Main Program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = reverse_number(number=number)
        print(f"Reversed number: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
