"""Generate a numbers using a loop."""

from collections.abc import Iterator


def generate_numbers(limit: int) -> Iterator[int]:
    """Generate the numbers."""
    for number in range(limit):
        yield number


numbers = generate_numbers(limit=5)

print(next(numbers))
print(next(numbers))
print("In for loop")
for number in numbers:
    print(number)
