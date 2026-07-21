"""Sum of odd numbers."""

from get_gcd import validate_number


def sum_of_odd_numbers(number: int) -> int:
    """
    Return the sum of all odd numbers from 1 to the input number.

    Args:
        number (int): Input number.

    Returns:
        int: The sum of odd numbers.
    """
    odd_count = (number + 1) // 2
    return odd_count * odd_count


def main() -> None:
    """Run the Main Program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number, field_name="number")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = sum_of_odd_numbers(number=number)
        print(f"Sum of odd numbers from 1 to {number}: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
