"""Calculate area of circle."""

from math import pi

try:
    radius = float(input("Enter the radius of circle: "))
    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    area_of_circle = pi * radius ** 2
    print(f"Area of circle: {area_of_circle:.2f}")
finally:
    print("Operation completed.")
