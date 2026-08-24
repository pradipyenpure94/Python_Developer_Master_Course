"""Calculate the area of a triangle."""


try:
    height = float(input("Enter the height of triangle: "))
    base = float(input("Enter the base of triangle: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nCalculation cancelled by the user.")
else:
    area_of_triangle = height * base / 2
    print(f"Area of triangle: {area_of_triangle:.2f}")
