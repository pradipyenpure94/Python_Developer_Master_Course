"""Find missing number."""

MIN_NUMBER_LIMIT = 1


def find_missing_number(numbers: list[int]) -> int:
    """
    Return the missing integer in the sequence starting
    from 1 up to the largest value.

    Args:
        numbers (list[int]): Input numbers list.

    Returns:
        int: The missing number if found; otherwise, -1.
    """
    if not numbers:
        raise ValueError("List cannot be empty.")

    if any(number < MIN_NUMBER_LIMIT for number in numbers):
        raise ValueError(
            f"Number must be greater than or equal to {MIN_NUMBER_LIMIT}."
        )

    distinct_numbers = set(numbers)
    if len(numbers) != len(distinct_numbers):
        raise ValueError("Duplicate numbers are not allowed.")

    max_number = max(numbers)
    for number in range(MIN_NUMBER_LIMIT, max_number + 1):
        if number not in distinct_numbers:
            return number

    return -1


def main() -> None:
    """Run the Main Program."""
    try:
        numbers = [2, 3, 5, 4]
        result = find_missing_number(numbers=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Missing number: {result}")


if __name__ == "__main__":
    main()
