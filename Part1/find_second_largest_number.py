"""Find the second largest number."""


def find_second_largest_number(nums: list[int]) -> int:
    """
    Return the second largest number in a list.

    Args:
        nums (list[int]): Input list of numbers.

    Returns:
        int: The second largest unique number in the list.

    Raises:
        ValueError: If the list contains less than two unique numbers.
    """
    if not nums or len(set(nums)) < 2:
        raise ValueError("List must contain at least two unique numbers.")

    first_number = second_number = float('-inf')

    for number in nums:
        if number > first_number:
            second_number = first_number
            first_number = number
        elif number > second_number and number != first_number:
            second_number = number

    return second_number


if __name__ == "__main__":
    numbers = [1, 1, 2]
    print(f"Input numbers: {numbers}")

    try:
        result = find_second_largest_number(nums=numbers)
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Second Largest number: {result}")
    finally:
        print("Operation completed.")
