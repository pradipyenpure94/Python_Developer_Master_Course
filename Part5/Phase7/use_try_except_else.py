"""Use try-except-else."""


def addition(first_number: int, second_number: int) -> int:
    """Return the addition of two numbers."""
    return first_number + second_number


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    result = addition(first_number=first_number, second_number=second_number)
except ValueError as error:
    print(f"Error: {error}")
else:
    print(f"Addition: {result}")
