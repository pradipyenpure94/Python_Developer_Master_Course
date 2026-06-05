"""Lambda for cube."""


def cube_number(num: int) -> int:
    """
    Return the cube of number.

    Args:
        num (int): Input number.

    Returns:
        int: Cube of number.
    """
    return (lambda x: x ** 3)(num)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = cube_number(num=number)
        print(f"Cube of number: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
