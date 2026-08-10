"""__mul__() method."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """Calculate and return the area of rectangle."""
        return self.width * self.length

    def __mul__(self, other: object) -> float:
        """Return the product of the areas of two rectangles."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.calculate_area() * other.calculate_area()


def main() -> None:
    """Run the main program."""
    rectangle_obj1 = Rectangle(length=10, width=35)
    rectangle_obj2 = Rectangle(length=25, width=50)
    product_area = rectangle_obj1 * rectangle_obj2
    print(f"Product of rectangle areas: {product_area:.2f}")


if __name__ == "__main__":
    main()
