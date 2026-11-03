"""Calculate the area and circumference of a circle."""

from math import pi

radius = float(input("Enter the radius of circle: "))

area_of_circle = pi * (radius ** 2)
circumference_of_circle = 2 * pi * radius
print(f"Area of circle        : {area_of_circle:.2f}")
print(f"Area of circumference : {circumference_of_circle:.2f}")
