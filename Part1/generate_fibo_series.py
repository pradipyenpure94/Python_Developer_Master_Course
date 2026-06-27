"""Generate fibonacci series."""


def generate_fibonacci_series(num: int) -> None:
    """
    Generate fibonacci series.

    Args:
        num (int): Input number.

    Returns:
        None.
    """
    if num < 0:
        raise ValueError("Fibonacci is not defined for negative number.")
    a, b = 0, 1
    for _ in range(num):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        generate_fibonacci_series(num=number)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        print("Operation completed.")
