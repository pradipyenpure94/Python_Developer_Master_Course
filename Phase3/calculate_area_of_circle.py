"""Calculate area of circle."""

from math import pi


def calculate_area_of_circle(radius: float) -> float:
    """Return the area of circle.

    Args:
        radius (float): Radius of circle.

    Returns:
        float: Area of circle.
    """
    return pi * radius ** 2


if __name__ == "__main__":
    try:
        r = float(input("Enter radius of circle: "))
        result = calculate_area_of_circle(radius=r)
        print(f"Area of circle: {result:0.2f}")
    except ValueError:
        print("Invalid input! Please enter a number.")
