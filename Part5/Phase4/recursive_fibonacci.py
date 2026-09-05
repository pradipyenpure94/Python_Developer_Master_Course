"""Recursive Fibonacci."""


def recursive_fibonacci(number: int) -> int:
    """Return the Fibonacci of 'N' th terms."""
    if number < 0:
        raise ValueError("Fibonacci number must be non-negative.")
    if number <= 1:
        return number
    return recursive_fibonacci(
        number=number - 1
    ) + recursive_fibonacci(number=number - 2)


if __name__ == "__main__":
    try:
        number = int(input("Enter the number: "))
        result = recursive_fibonacci(number=number)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Fibonacci of {number} is: {result}")
