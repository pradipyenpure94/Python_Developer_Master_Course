"""Create Shape ---> Circle, Rectangle."""


class Shape:
    """Represent a shape."""

    def __init__(self, name: str) -> None:
        self.name = name


class Circle(Shape):
    """Represent a circle."""

    def draw(self) -> None:
        """Display draw method."""
        print(f"Draw a {self.name}.")


class Rectangle(Shape):
    """Represent a rectangle."""

    def draw(self) -> None:
        """Display draw method."""
        print(f"Draw a {self.name}.")


def main() -> None:
    """Run the main program."""

    rect = Rectangle(name="Rectangle")
    rect.draw()

    circle = Circle(name="Circle")
    circle.draw()


if __name__ == "__main__":
    main()
