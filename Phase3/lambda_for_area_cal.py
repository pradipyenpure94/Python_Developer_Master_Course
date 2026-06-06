"""Lambda for area calculation."""


def area_of_rectangle(length: float, width: float) -> float:
    """
    Return the area of rectangle.

    Args:
        length (float): Input length of rectangle.
        width (float): Input width of rectangle.

    Returns:
        float: Area of rectangle.
    """
    area_rectangle = lambda l: lambda w: l * w
    return area_rectangle(length)(width)


if __name__ == "__main__":
    try:
        rect_length = float(input("Enter length of rectangle: "))
        rect_width = float(input("Enter width of rectangle: "))
        result = area_of_rectangle(length=rect_length, width=rect_width)
        print(f"Area of rectangle: {result}")
    except ValueError:
        print("Invalid input! Please enter a number.")
