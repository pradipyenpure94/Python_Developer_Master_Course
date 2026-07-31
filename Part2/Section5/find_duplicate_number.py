"""Find duplicate number."""


def find_duplicate_numbers(numbers: list[int]) -> list[int]:
    """
    Return the duplicate numbers from the input numbers list.

    Args:
        numbers (list[int]): Input numbers list.

    Returns:
        list[int]: A list containing each duplicate number exactly once.
    """
    if not numbers:
        raise ValueError("List cannot be empty.")

    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    return [number for number, count in frequency.items() if count > 1]


def main() -> None:
    """Run the Main Program."""
    numbers = [1, 2, 3, 1, 5, 6, 4, 2, 5, 6, "tree", "tree"]
    result = find_duplicate_numbers(numbers=numbers)
    print(f"Duplicate numbers: {result}")


if __name__ == "__main__":
    main()
