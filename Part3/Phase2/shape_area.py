"""
Shape Area

Create:

    Shape
    ├── Circle
    ├── Rectangle
    └── Triangle

Each class should override:

    calculate_area()
"""
from math import pi


class Shape:
    """Represent a shape."""

    def __init__(self, name: str) -> None:
        self.name = name


class Circle(Shape):
    """Represent a circle."""
    def __init__(self, name: str, radius: float) -> None:
        super().__init__(name=name)
        self.radius = radius

    def calculate_area(self) -> float:
        """Return the area of the circle."""
        return pi * (self.radius ** 2)


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, name: str, length: float, width: float) -> None:
        super().__init__(name=name)
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """Return the area of the rectangle."""
        return self.length * self.width


class Triangle(Shape):
    """Represent a triangle."""

    def __init__(self, name: str, base: float, height: float) -> None:
        super().__init__(name=name)
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        """Return the area of the triangle."""
        return (self.base * self.height) / 2


def main() -> None:
    """Run the main program."""
    shapes = [
        Circle(name="Circle", radius=2.5),
        Rectangle(name="Rectangle", length=2.5, width=6),
        Triangle(name="Triangle", base=5, height=5.6)
    ]

    for shape in shapes:
        area = shape.calculate_area()
        print(f"Area: {area:.2f}")


if __name__ == "__main__":
    main()
