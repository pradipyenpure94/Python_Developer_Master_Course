"""Recursive binary search."""


def binary_search_recursive(
    numbers: list[int],
    target: int,
    low: int,
    high: int
) -> int:
    """Return the index of target using recursive binary search."""
    if high < low:
        return -1

    mid = low + (high - low) // 2

    if numbers[mid] == target:
        return mid

    elif numbers[mid] > target:
        return binary_search_recursive(
            numbers=numbers,
            target=target,
            low=low,
            high=mid - 1
        )
    else:
        return binary_search_recursive(
            numbers=numbers,
            target=target,
            low=mid + 1,
            high=high
        )


if __name__ == "__main__":
    numbers = [1, 0, 1, 0, 1, 9, 9, 3]
    numbers.sort()
    print(f"Numbers      : {numbers}")
    target = 3
    print(f"Target Value : {target}")
    start_index = 0
    end_index = len(numbers) - 1

    result = binary_search_recursive(
        numbers=numbers,
        target=target,
        low=start_index,
        high=end_index
    )

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print(f"Element not found at index {result}")
