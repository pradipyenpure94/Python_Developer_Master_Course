"""Convert tuple to list."""


def convert_tuple_to_list(values: tuple[str, ...]) -> list[str]:
    """
    Return a new list created from the input tuple.

    Args:
        values (tuple[str, ...]): Input values.

    Returns:
        list[str]: The converted list.

    Raises:
        ValueError: If the input tuple is empty.
    """
    if not values:
        raise ValueError("Input tuple cannot be empty.")

    return list(values)


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = tuple(
            input("Enter the numbers separated by spaces: ").split()
        )

        result = convert_tuple_to_list(values=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Tuple converted to list: {result}")


if __name__ == "__main__":
    main()
