"""Find pair with target sum."""


def validate_numbers_list(numbers: list[int]) -> None:
    """Validate the numbers list."""
    if not numbers:
        raise ValueError("Numbers list cannot be empty.")
    if len(numbers) != len(set(numbers)):
        raise ValueError("Duplicate numbers not allowed.")


def find_pair_with_target_sum(
    numbers: list[int],
    target: int
) -> tuple[int, int] | None:
    """
    Return the first pair of numbers whose sum equals the target.

    Args:
        numbers (list[int]): Input numbers list.
        target (int): Target sum.

    Returns:
        tuple[int, int] | None:
            The first matching pair if found; otherwise, None.
    """
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return (complement, number)
        seen.add(number)

    return None


def main() -> None:
    """Run the Main Program."""
    try:
        target = 3
        numbers = [1, 2, 3, 4, 5]
        validate_numbers_list(numbers=numbers)

    except ValueError as error:
        print(f"Error: {error}")
    else:
        result = find_pair_with_target_sum(numbers=numbers, target=target)
        if result is None:
            print("No matching pair found.")
        else:
            print(f"Pairs: {result}")


if __name__ == "__main__":
    main()
