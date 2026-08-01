"""Create tuple."""


def create_tuple(values: list[str]) -> tuple[str, ...]:
    """
    Return the created tuple from the input values.

    Args:
        values (list[str]): Input values.

    Returns:
        tuple[str, ...]: The created tuple.

    Raises:
        ValueError: If the input values list is empty.
    """
    if not values:
        raise ValueError("Input cannot be empty.")
    return tuple(values)


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = input("Enter the numbers separated by spaces: ").split()
        result = create_tuple(values=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"The created tuple is: {result}")


if __name__ == "__main__":
    main()
