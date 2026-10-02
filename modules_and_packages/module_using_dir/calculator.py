"""Arithmetic operation functions."""

from numbers import Real


def add(first_number: Real, second_number: Real) -> Real:
    """Return the addition of two numbers."""

    return first_number + second_number


def div(first_number: Real, second_number: Real) -> Real:
    """Return the division of two numbers."""

    return first_number + second_number


MIN_DEPOSIT_AMOUNT = 100


class Employee:
    """Represent an employee."""
    def __init__(self, name: str) -> None:
        self.name = name
