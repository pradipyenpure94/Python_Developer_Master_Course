"""Generate strings with length greater than 5."""


import random
import string
from collections.abc import Iterator


def generate_random_strings() -> Iterator[str]:
    """Generate random strings with length greater than 5."""
    yield "".join(random.choices(string.ascii_letters, k=6))


if __name__ == "__main__":
    iterator = generate_random_strings()
    for random_string in iterator:
        print(random_string)
