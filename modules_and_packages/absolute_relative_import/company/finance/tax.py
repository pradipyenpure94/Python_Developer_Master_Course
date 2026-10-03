"""Design and develop a function."""

from numbers import Real

TAX = 18


def calculate_tax(salary: Real) -> Real:
    """Calculate tax on salary."""

    return salary * TAX / 100
