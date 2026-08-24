"""Calculate the area and perimeter of a rectangle."""


try:
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of rectangle: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    area_of_rectangle = length * width
    print(f"Area of Rectangle      : {area_of_rectangle:.2f}")
    perimeter_of_rectangle = 2 * (length + width)
    print(f"Perimeter of Rectangle : {perimeter_of_rectangle:.2f}")
