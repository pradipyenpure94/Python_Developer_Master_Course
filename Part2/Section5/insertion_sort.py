"""Insertion sort."""

from smallest_element import validate_numbers_list


def insertion_sort(numbers: list[int | float]) -> list[int | float]:
    """
    Return the sorted numbers list using insertion sort.

    Args:
        numbers (list[int | float]): Input numbers list.

    Returns:
        list[int | float]: The sorted list using insertion sort.
    """
    n = len(numbers)

    if n <= 1:
        return numbers

    for i in range(1, n):
        key = numbers[i]
        j = i - 1

        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

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
        result = insertion_sort(numbers=numbers)
        print(f"Sorted list (insertion sort): {result}")


if __name__ == "__main__":
    main()
