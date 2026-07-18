"""Palindrome number."""

from reverse_number import reverse_number

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


def is_palindrome_number(number: int) -> bool:
    """
    Check whether the number is a palindrome.

    Args:
        number (int): Input number.

    Returns:
        bool: True if the number is a palindrome; otherwise, False.
    """
    return number == reverse_number(number=number)


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
        if is_palindrome_number(number=number):
            print(f"{number} is a palindrome number.")
        else:
            print(f"{number} is not a palindrome.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
