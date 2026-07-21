"""Sum of even numbers."""

from get_gcd import validate_number


def sum_of_even_numbers(number: int) -> int:
    """
    Return the sum of the even numbers from 1 to the input number.

    Args:
        number (int): Input number.

    Returns:
        int: Sum of even numbers.
    """
    even_count = number // 2
    return even_count * (even_count + 1)


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
        result = sum_of_even_numbers(number=number)
        print(f"The sum of even numbers from 1 to {number}: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
