"""Generator delegation using yield from."""


from collections.abc import Iterator


def generate_numbers(limit: int) -> Iterator[int]:
    """Generate numbers."""
    yield from range(1, limit + 1)


if __name__ == "__main__":
    iterator = generate_numbers(limit=5)
    for number in iterator:
        print(number)
