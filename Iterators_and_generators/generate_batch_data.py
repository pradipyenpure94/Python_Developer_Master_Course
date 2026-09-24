"""Generator for batching data."""

from collections.abc import Iterator


def generate_batching_data(
    numbers: list[int],
    batch_size: int = 3
) -> Iterator[list[int]]:
    """Generate batches of data based on the given batch size."""
    if batch_size <= 0:
        raise ValueError("Batch size must be greater than zero.")

    for index in range(0, len(numbers), batch_size):
        yield numbers[index: index + batch_size]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        iterator = generate_batching_data(numbers=nums, batch_size=4)

        for batch in iterator:
            print(batch)

    except ValueError as error:
        print(f"Error: {error}")
