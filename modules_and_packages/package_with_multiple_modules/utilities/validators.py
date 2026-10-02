"""Design and develop validation functions."""

from numbers import Real


def is_positive(number: Real) -> bool:
    """Return True, if the number is positive otherwise False."""
    return number > 0


def is_negative(number: Real) -> bool:
    """Return True, if the number is negative otherwise False."""
    return number < 0
