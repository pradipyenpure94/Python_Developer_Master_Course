"""
Calculator — Method Overloading

Create an add() method using *args that can add:

    - 2 numbers
    - 3 numbers
    - 5 numbers
    - any number of numbers

Understand how Python achieves overloading using variable arguments.
"""


class Calculator:
    """Represent a calculator."""

    def add(self, *args: float) -> float:
        """Return the addition of N numbers."""
        return sum(args)


def main() -> None:
    """Run the main program."""
    calculator = Calculator()

    result = calculator.add(10, 20, 56, 45, 78, 96.56)

    print(f"Addition: {result}")


if __name__ == "__main__":
    main()
