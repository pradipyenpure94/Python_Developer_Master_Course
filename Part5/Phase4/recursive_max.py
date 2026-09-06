"""Recursive list maximum."""


def find_recursive_max(numbers: list[int], index: int = 0) -> int:
    """Return the maximum number from input numbers list."""
    if not numbers:
        raise ValueError("List is empty.")
    if index == len(numbers) - 1:
        return numbers[index]

    max_of_rest = find_recursive_max(numbers=numbers, index=index + 1)
    return max(numbers[index], max_of_rest)


if __name__ == "__main__":
    numbers = [1, 9, 9, 3]
    result = find_recursive_max(numbers=numbers)
    print(f"Maximum number: {result}")
