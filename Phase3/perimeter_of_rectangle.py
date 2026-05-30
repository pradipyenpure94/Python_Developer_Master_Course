"""Perimeter of rectangle."""


def calculate_perimeter_of_rectangle(length: float, width: float) -> float:
    """
    Return the perimeter of rectangle.

    Args:
        length (float): Input as length of rectangle.
        width (float): Input as width of rectangle.

    Returns:
        float: Perimeter of rectangle.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return 2 * (length + width)


if __name__ == "__main__":
    try:
        l = float(input("Enter length of rectangle: "))
        w = float(input("Enter width of rectangle: "))
        result = calculate_perimeter_of_rectangle(length=l, width=w)
        print(f"Perimeter of rectangle: {result}")
    except ValueError as error:
        print(f"Error: {error}")
