"""Count frequency."""

from smallest_element import validate_numbers_list


def count_frequency_of_element(
    numbers: list[int | float]
) -> dict[int | float, int]:
    """
    Return the frequency count of each element in the input numbers list.

    Args:
        numbers (list[int | float]): Input numbers list.

    Returns:
        dict[int | float, int]: The frequency count of each element.
    """
    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    return frequency


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [1, 0, 1, 0, 1, 9, 9, 3]
        validate_numbers_list(numbers=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = count_frequency_of_element(numbers=numbers)
        print(f"Frequency count: {result}")


if __name__ == "__main__":
    main()
