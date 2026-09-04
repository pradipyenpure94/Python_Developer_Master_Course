"""Calculate area of circle."""

from math import pi


def calculate_area_of_circle(radius: float) -> float:
    """
    Return the area of circle.

    Args:
        radius: Input radius of circle.

    Returns:
        float: Area of circle.
    """
    return pi * (radius ** 2)


if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of circle: "))

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = calculate_area_of_circle(radius=radius)
        print(f"Area of Circle: {result:.2f}")
