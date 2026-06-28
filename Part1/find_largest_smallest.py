"""Find the smallest and largest element in a list."""


def find_smallest_largest_element(elements: list[int]) -> tuple[int, int]:
    """
    Return the smallest and largest element in a list.

    Args:
        elements (list[int]): Input elements list.

    Returns:
        tuple[int, int]: Smallest and largest elements.

    Raises:
        ValueError: If the list is empty.
    """
    if not elements:
        raise ValueError("List cannot be empty.")

    smallest = elements[0]
    largest = elements[0]

    for number in elements[1:]:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number

    return smallest, largest


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Input numbers: {numbers}")

    try:
        smallest, largest = find_smallest_largest_element(elements=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Smallest: {smallest}\n"
              f"Largest: {largest}")
    finally:
        print("Operation completed.")
