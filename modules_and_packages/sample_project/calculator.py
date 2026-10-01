"""Custom arithmetic functions."""

from math import prod
from numbers import Real


def addition(*args: Real) -> Real:
    """Return the addition of N numbers."""
    return sum(args)


def multiplication(*args: Real) -> Real:
    """Return the multiplication of N numbers."""
    return prod(args)


def division(first_number: Real, second_number: Real) -> float:
    """Return the division of two numbers."""
    return first_number / second_number
