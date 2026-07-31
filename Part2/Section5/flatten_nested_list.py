"""Flatten nested list."""


def flatten_list(numbers: list[int | list[int]]) -> list[int]:
    """
    Return a new flattened list from the nested input list.

    Args:
        numbers (list[int | list[int]]): Nested input list.

    Returns:
        list[int]: A new flattened list.
    """
    flat_list = []

    for number in numbers:
        if isinstance(number, list):
            flat_list.extend(flatten_list(numbers=number))
        else:
            flat_list.append(number)

    return flat_list


def main() -> None:
    """Run the Main Program."""
    numbers = [1, [4, 5, [1, 2], [3]], [4, 5, 6, 7, 8], 10]
    result = flatten_list(numbers=numbers)
    print(f"Flat list: {result}")


if __name__ == "__main__":
    main()
