"""Simple Generator."""


def generate_numbers():
    """Create the simple generator."""
    yield 10
    yield 20
    yield 20

numbers = generate_numbers()

print(next(numbers))
print("In for loop")
for number in numbers:
    print(number)
