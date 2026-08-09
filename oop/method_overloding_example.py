"""
Example of method overloading.
Python does not support method overloading
but we can acheive method overloading in python
"""


class Calculator:
    """Represent a claculator."""

    def add(self, *numbers) -> float:
        """The addition of input numbers."""
        return sum(numbers)


def filtered_numbers(numbers: list[str]) -> tuple[float, ...]:
    """Filter the numbers to only integers and floats."""
    result = []
    for num in numbers:
        try:
            result.append(float(num))
        except ValueError:
            continue

    return tuple(result)


def main() -> None:
    """Run the main program."""
    numbers = input("Enter the numbers separated by spaces: ").split()
    nums = filtered_numbers(numbers=numbers)
    calculator_obj = Calculator()
    result = calculator_obj.add(*nums)
    print(f"Addition of input numbers: {result}")


if __name__ == "__main__":
    main()
