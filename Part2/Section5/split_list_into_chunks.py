"""Split list into chunks."""

from smallest_element import validate_numbers_list


def validate_chunk_size(chunk_size: int) -> None:
    """Validate that chunk size is greater than zero."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")


def split_list_into_chunks(
    numbers: list[int | float], chunk_size: int = 3
) -> list[list[int | float]]:
    """
    Return a new list split into chunks of the specified size.

    Args:
        numbers (list[int | float]): Input numbers list.
        chunk_size (int, optional): Chunk size. Defaults to 3.

    Returns:
        list[list[int | float]]: A new nested list.
    """
    return [
        numbers[index:index + chunk_size]
        for index in range(0, len(numbers), chunk_size)
    ]


def main() -> None:
    """Run the main program."""
    try:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        validate_numbers_list(numbers=numbers)
        chunk_size = int(input("Enter the chunk size: "))
        validate_chunk_size(chunk_size=chunk_size)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = split_list_into_chunks(
            numbers=numbers,
            chunk_size=chunk_size
        )
        print(f"List split into chunks: {result}")


if __name__ == "__main__":
    main()
