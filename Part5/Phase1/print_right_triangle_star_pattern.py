"""Print a right triangle star pattern."""


try:
    size = int(input("Enter the size: "))
    if size <= 0:
        raise ValueError("Size must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for row in range(1, size + 1):
        print(" * " * row)
