"""Print square star pattern."""

try:
    size = int(input("Enter the square size: "))
    if size <= 0:
        raise ValueError("Size must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    print("Square star pattern:")
    for colum in range(size):
        print(" * " * size)
