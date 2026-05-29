"""Find cube using function."""


def cube(number: int) -> int:
    """Return the cube of a number.

    Args:
        number (int): input number.

    Returns:
        int: Cube of the number.
    """
    return number ** 3


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"Cube of {num} is: {cube(number=num)}")
    except ValueError:
        print("Invalid input! Please enter a valid input.")
