"""Calculate the area and perimeter of a square."""


try:
    side = float(input("Enter the side of square: "))
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    perimeter_of_square = 4 * side
    print(f"Perimeter of square: {perimeter_of_square:.2f}")
    area_of_square = side ** 2
    print(f"Area of square: {area_of_square:.2f}")
