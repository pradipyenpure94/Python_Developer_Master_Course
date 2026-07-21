"""Sum of first N numbers."""

from get_gcd import validate_number


def sum_of_first_n_numbers(number: int) -> int:
    """
    Return the sum of the first N numbers.

    Args:
        number (int): Input number.

    Returns:
        int: The sum of the first N numbers.
    """
    return number * (number + 1) // 2


def main() -> None:
    """Run the Main Program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number, field_name="Number")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = sum_of_first_n_numbers(number=number)
        print(f"Sum of first N numbers: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
