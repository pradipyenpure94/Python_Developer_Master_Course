"""Calculate area of circle."""

from math import pi

try:
    radius = float(input("Enter radius: "))
    if radius < 0:
        print("Radius cannot be negative!")
    else:
        area = pi * radius ** 2
        print(f"Area of circle: {area:.2f}")
except ValueError:
    print("Invalid input! Please enter a number.")
