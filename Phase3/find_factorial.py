"""Find factorial using reduce."""

from functools import reduce
from operator import mul


def find_factorial(num: int) -> int:
    """
    Return the factorial number.

    Args:
        num (int): Input number.

    Returns:
        int: Factorial of the input number.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return reduce(mul, range(1, num + 1), 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = find_factorial(num=number)
        print(f"Factorial of {number} is: {result}")
    except ValueError as error:
        print(f"Error: {error}")
