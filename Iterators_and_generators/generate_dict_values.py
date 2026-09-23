"""Generate dictionary values selectively."""

from collections.abc import Iterator


def generate_dictionary(dictionary: dict[str, int]
                        ) -> Iterator[dict[str, int]]:
    """Generate dictionary values selectively."""
    yield {key: value for key, value in dictionary.items() if value > 30}


if __name__ == "__main__":
    data = {"Cherry": 25, "Apple": 35, "Banana": 45}
    iterator = generate_dictionary(dictionary=data)
    print(next(iterator))
