"""Common elements."""

from smallest_element import validate_numbers_list


def find_common_elements(
    list1: list[int | float],
    list2: list[int | float]
) -> list[int | float]:
    """
    Return the distinct common elements from both input lists.

    Args:
        list1 (list[int | float]): First input list.
        list2 (list[int | float]): Second input list.

    Returns:
        list[int | float]: The distinct common elements from both input lists.
    """
    common_elements = []
    seen = set()

    for item in list1:
        if item in list2 and item not in seen:
            common_elements.append(item)
            seen.add(item)

    return common_elements


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
        result = find_common_elements(list1=prime_numbers, list2=even_numbers)
        print(f"Distinct common elements: {result}")


if __name__ == "__main__":
    main()
