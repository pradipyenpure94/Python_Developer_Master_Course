"""Example of Abstraction."""

from abc import ABC, abstractmethod
from math import pi

MIN_DIMENSION = 1


def validate_positive_dimension(value: float, field_name: str) -> None:
    """Validate that a dimension is at least the minimum value."""
    if value < MIN_DIMENSION:
        raise ValueError(f"{field_name} must be at least {MIN_DIMENSION}.")


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def calculate_area(self) -> float:
        """Calculate and return the area."""
        raise NotImplementedError


class Rectangle(Shape):
    """Rectangle class."""
    def __init__(self, width: float, length: float) -> None:
        validate_positive_dimension(value=length, field_name="Length")
        validate_positive_dimension(value=width, field_name="Width")

        self.width = width
        self.length = length

    def calculate_area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.length


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius: float) -> None:
        validate_positive_dimension(value=radius, field_name="Radius")
        self.radius = radius

    def calculate_area(self) -> float:
        """Calculate the area of the circle."""
        return pi * (self.radius ** 2)


def main() -> None:
    """Run the main program."""
    try:
        width = float(input("Enter the width of rectangle: "))
        length = float(input("Enter the length of rectangle: "))
        rectangle_obj = Rectangle(width=width, length=length)
        print(f"Area of rectangle: {rectangle_obj.calculate_area():.2f}\n")

        radius = float(input("Enter the radius of circle: "))
        circle_obj = Circle(radius=radius)
        print(f"Area of circle: {circle_obj.calculate_area():.2f}")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")


if __name__ == "__main__":
    main()
