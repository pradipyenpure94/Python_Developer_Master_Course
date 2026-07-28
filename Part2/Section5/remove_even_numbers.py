"""Remove even numbers."""


def validate_integer_numbers(numbers: list[int]) -> None:
    """Validate the input numbers list."""
    if not numbers:
        raise ValueError("List cannot be empty.")
    if not all(
        isinstance(number, int) and not isinstance(number, bool)
        for number in numbers
    ):
        raise ValueError("List must contain only integers.")


def remove_even_numbers(numbers: list[int]) -> list[int]:
    """
    Remove the even numbers from the input numbers list.

    Args:
        numbers (list[int]): Input numbers list.

    Returns:
        list[int]: A new list containing only odd numbers.
    """
    return [number for number in numbers if number % 2 == 1]


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
        result = remove_even_numbers(numbers=numbers)
        print(f"List after removing even numbers: {result}")


if __name__ == "__main__":
    main()
