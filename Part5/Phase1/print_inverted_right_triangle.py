"""Print an inverted right triangle."""


try:
    size = int(input("Enter the size of triangle: "))
    if size <= 0:
        raise ValueError("Size must be greater than zero.")
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for row in range(size, 0, -1):
        print(" * " * row)
