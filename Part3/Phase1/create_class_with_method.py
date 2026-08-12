"""Create a Rectangle class and calculate area/perimeter."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def calculate_rectangle_area(self) -> float:
        """Return the area of rectangle."""
        return self.length * self.width

    def calculate_rectangle_perimeter(self) -> float:
        """Return the rectangle of perimeter."""
        return 2 * (self.length + self.width)


def main() -> None:
    """Run the main program."""
    rectangle_obj = Rectangle(length=2.5, width=2)

    print(f"Area of rectangle: {rectangle_obj.calculate_rectangle_area():.2f}")
    print(
        "Perimeter of rectangle: "
        f"{rectangle_obj.calculate_rectangle_perimeter():.2f}")


if __name__ == "__main__":
    main()
