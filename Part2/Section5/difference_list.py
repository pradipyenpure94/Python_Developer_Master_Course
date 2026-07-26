"""Difference between lists."""

from smallest_element import validate_numbers_list

def find_difference(
    list1: list[int | float],
    list2: list[int | float]
) -> list[int | float]:
    """
    Return the distinct elements present in the first input list
    but not in the second input list.

    Args:
        list1 (list[int | float]): First input list.
        list2 (list[int | float]): Second input list.

    Returns:
        list[int | float]: The distinct elements present in the
        first input list but not in the second input list.
    """
    difference_list = []
    seen = set()
    lookup = set(list2)

    for item in list1:
        if item not in lookup and item not in seen:
            difference_list.append(item)
            seen.add(item)

    return difference_list


def main() -> None:
    """Run the Main Program."""
    try:
        prime_numbers = [2, 3, 5, 7, 11, 13]
        validate_numbers_list(numbers=prime_numbers)
        even_numbers = [2, 4, 6, 8, 10]
        validate_numbers_list(numbers=even_numbers)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = find_difference(list1=prime_numbers, list2=even_numbers)
        print(f"Difference: {result}")


if __name__ == "__main__":
    main()
