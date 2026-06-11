"""Recursive fibonacci."""


def recursive_fibonacci(num: int) -> int:
    """
    Return the fibonacci number at the given position.

    Args:
        num (int): Input number.

    Returns:
        int: Fibonacci number at the given position.
    """
    if num < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if num <= 1:
        return num
    return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = recursive_fibonacci(num=number)
        print(f"Fibonacci number: {result}")
    except ValueError as error:
        print(f"Error: {error}")
