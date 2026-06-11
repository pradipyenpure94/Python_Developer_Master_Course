"""Recursive factorial."""


def recursive_factorial(num: int) -> int:
    """
    Return the factorial of the input number.

    Args:
        num (int): Input number.

    Returns:
        int: Factorial of the input number.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if num <= 0:
        return 1
    return num * recursive_factorial(num - 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = recursive_factorial(num=number)
        print(f"Factorial of {number} is: {result}")
    except ValueError as error:
        print(f"Error: {error}")
