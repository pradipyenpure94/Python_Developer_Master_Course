"""
Rectangle Class

Create a Rectangle class and calculate:

    area
    perimeter
"""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def calculate_rectangle_area(self) -> float:
        """Calculate and return the area of rectangle."""
        return self.length * self.width

    def calculate_rectangle_perimeter(self) -> float:
        """Calculate and return the perimeter of rectangle."""
        return 2 * (self.length + self.width)


def main() -> None:
    """Run the main program."""
    rectangle_object = Rectangle(length=5, width=2.5)

    area = rectangle_object.calculate_rectangle_area()
    print(f"Area of Rectangle      : {area}")

    perimeter = rectangle_object.calculate_rectangle_perimeter()
    print(f"Perimeter of Rectangle : {perimeter}")


if __name__ == "__main__":
    main()
