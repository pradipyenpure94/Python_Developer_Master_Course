"""Find square using function."""


def square(number: int) -> int:
    """Return the square of number.
    Args:
        number (int): input number.
    Returns:
        int: Square of number.
    """
    return number * number


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"Square of {num} is: {square(number=num)}")
    except ValueError:
        print("Invalid input! Please enter a valid input.")
