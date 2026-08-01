"""Count occurrences."""


def count_occurrences(values: list[str]) -> dict[str, int]:
    """
    Return a dictionary mapping each element to its occurrence count.

    Args:
        values (list[str]): Input values.

    Returns:
        dict[str, int]: A dictionary mapping each element to its occurrence
        count.

    Raises:
        ValueError: If the input list is empty.
    """
    if not values:
        raise ValueError("Input list values cannot be empty.")

    frequency = {}

    for item in values:
        frequency[item] = frequency.get(item, 0) + 1

    return frequency


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = input("Enter the numbers separated by spaces: ").split()
        result = count_occurrences(values=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Element occurrences: {result}")


if __name__ == "__main__":
    main()
