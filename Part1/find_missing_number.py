"""Find missing numbers from a list containing numbers."""


def find_all_missing_numbers(nums: list[int]) -> list[int]:
    """
    Return the missing numbers from the input list.

    Args:
        nums (list[int]): Input numbers list.

    Returns:
        list[int]: Missing number(s) from the input numbers list.

    Raises:
        ValueError: If the input contains fewer than two unique numbers.
    """
    if len(set(nums)) < 2:
        raise ValueError("Expected numbers not found.")

    full_set = set(range(min(nums), max(nums) + 1))
    actual_set = set(nums)
    missing_numbers = list(full_set - actual_set)
    return missing_numbers


if __name__ == "__main__":
    numbers = [1, 3, 5, 6]
    print(f"Numbers: {numbers}")

    try:
        result = find_all_missing_numbers(nums=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Missing number(s): {result}")
    finally:
        print("Operation completed.")
