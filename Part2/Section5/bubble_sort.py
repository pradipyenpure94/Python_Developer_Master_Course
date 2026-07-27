"""Bubble sort."""

from smallest_element import validate_numbers_list


def bubble_sort(numbers: list[int | float]) -> list[int | float]:
    """
    Return the sorted list using bubble sort.

    Args:
        numbers (list[int | float]): Input numbers list.

    Returns:
        list[int | float]: The sorted list using bubble sort.
    """
    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


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
        result = bubble_sort(numbers=numbers)
        print(f"The sorted list (bubble sort): {result}")


if __name__ == "__main__":
    main()
