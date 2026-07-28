"""Remove odd numbers."""

from remove_even_numbers import validate_integer_numbers


def remove_odd_numbers(numbers: list[int]) -> list[int]:
    """
    Remove the odd numbers from the input numbers list.

    Args:
        numbers (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing only even numbers.
    """
    return [number for number in numbers if number % 2 == 0]


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        validate_integer_numbers(numbers=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = remove_odd_numbers(numbers=numbers)
        print(f"After removing odd numbers: {result}")


if __name__ == "__main__":
    main()
