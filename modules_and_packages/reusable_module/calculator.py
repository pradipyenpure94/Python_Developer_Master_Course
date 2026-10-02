"""Create reusable module with a Test Section."""

from numbers import Real


def square(number: Real) -> Real:
    return number ** 2


def cube(number: Real) -> Real:
    return number ** 3


if __name__ == "__main__":
    print("Testing module executed: ")
    print(square(number=5))
    print(cube(number=5))
