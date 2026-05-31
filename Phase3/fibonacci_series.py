"""Fibonacci series."""


def fibonacci_series(num: int) -> list[int]:
    """
    Return the fibonacci series of sequence.

    Args:
        num (int): Input number.

    Returns:
        list[int]: Fibonacci series of sequence.
    """
    if num < 0:
        raise ValueError("Negative number is not defined for fibonacci series.")
    fib = []
    a, b = 0, 1

    for _ in range(num):
        fib.append(a)
        a, b = b, a + b
    return fib


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = fibonacci_series(num=number)
        print(f"Fibonacci series: {result}")
    except ValueError as error:
        print(f"Error: {error}")
