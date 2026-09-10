"""Create abstract Shape class."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Represent a shape abstract base class."""

    @abstractmethod
    def calculate_area(self) -> float:
        """Calculate the area of the shape."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius: float) -> None:
        super().__init__()
        self.radius = radius

    def calculate_area(self) -> float:
        """Calculate the area of the circle."""
        return pi * self.radius ** 2


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.length * self.width


def main() -> None:
    """Run the main program."""
    shapes = [Circle(radius=5.2), Rectangle(length=5, width=2.5)]

    for shape in shapes:
        print(f"{shape.calculate_area():.2f}")


if __name__ == "__main__":
    main()
