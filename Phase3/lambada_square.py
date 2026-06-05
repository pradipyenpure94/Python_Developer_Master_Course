"""Lambda for square."""


def square_number(num: int) -> int:
    """Return the square of number.
    Args:
        num (int): Input number.
    Returns:
        int: Square of number.
    """
    square = lambda x: x * x
    return square(num)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = square_number(num=number)
    print(f"Square of number: {result}")
