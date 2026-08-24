"""Calculate area of a circle."""

from math import pi


try:
    radius = float(input("Enter the radius of circle: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    area_of_circle = pi * (radius ** 2)
    print(f"Area of Circle: {area_of_circle:.2f}")
