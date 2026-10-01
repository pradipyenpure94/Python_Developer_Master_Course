"""Design and develop math functions."""

from math import sqrt
from numbers import Real


def get_square_root_number(number: Real) -> Real:
    """Return the square root number."""

    return sqrt(number)


def get_square(number: Real) -> Real:
    """Return the square of the given number."""

    return number ** 2
