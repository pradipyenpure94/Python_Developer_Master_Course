"""Generate uppercase strings."""

import random
import string
from collections.abc import Iterator


def generate_uppercase_strings() -> Iterator[str]:
    """Generate random uppercase strings."""
    yield "".join(random.choices(string.ascii_uppercase, k=5))


if __name__ == "__main__":
    iterator = generate_uppercase_strings()
    print(next(iterator))
