"""Largest element."""


def validate_numbers_list(numbers: list[int | float]) -> None:
    """Validate the input numbers list."""
    if not numbers:
        raise ValueError("List cannot be empty.")
    if not all(
        isinstance(item, (int, float)) and not isinstance(item, bool)
        for item in numbers
    ):
        raise ValueError("List must contain only integers and floats.")


def find_largest_element(numbers: list[int | float]) -> int | float:
    """
    Return the largest element from the input numbers list.

    Args:
        numbers (list[int | float]): Input numbers list.

    Returns:
        int | float: The maximum element from the input number list.
    """
    return max(numbers)


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [10, 10, 19, 93, 30, 1, 19, 96]
        validate_numbers_list(numbers=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = find_largest_element(numbers=numbers)
        print(f"Largest element: {result}")


if __name__ == "__main__":
    main()
