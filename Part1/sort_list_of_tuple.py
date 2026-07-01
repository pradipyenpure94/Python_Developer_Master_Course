"""Sort list of tuples using lambda."""


def custom_sorted(data: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Return the list of tuples sorted by the second element.

    Args:
        data (list[tuple[int, int]]): Input list of tuples.

    Returns:
        list[tuple[int, int]]: A new list of tuples sorted by the second
        element.
    """
    return sorted(data, key=lambda item: item[1])


if __name__ == "__main__":
    input_data = [(5, 4), (1, 3), (6, 1)]
    print(f"Input data: {input_data}")
    result = custom_sorted(data=input_data)
    print(f"Sorted List of tuples: {result}")
