"""
Calculator Static Methods.

Create a Calculator class with static methods:

    - add()
    - subtract()
    - multiply()
    - divide()
"""


class Calculator:
    """Represent a calculator."""

    @staticmethod
    def add(first_number: float, second_number: float) -> float:
        """Return the addition of two numbers."""
        return first_number + second_number

    @staticmethod
    def subtract(first_number: float, second_number: float) -> float:
        """Return the subtraction of two numbers."""
        return first_number - second_number

    @staticmethod
    def multiply(first_number: float, second_number: float) -> float:
        """Return the multiplication of two numbers."""
        return first_number * second_number

    @staticmethod
    def divide(first_number: float, second_number: float) -> float:
        """Return the division of two numbers."""
        if second_number == 0:
            raise ValueError("Can not divide by zero.")
        return first_number / second_number


def main() -> None:
    """Run the main program."""
    try:
        result = Calculator.add(first_number=10, second_number=15)
        print(f"Addition        : {result:.2f}")

        result = Calculator.subtract(first_number=10, second_number=8)
        print(f"Subtraction     : {result:.2f}")

        result = Calculator.divide(first_number=45, second_number=0.5)
        print(f"Division        : {result:.2f}")

        result = Calculator.multiply(first_number=2.5, second_number=4)
        print(f"Multiplication  : {result:.2f}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
