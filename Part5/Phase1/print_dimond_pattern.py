"""Print a dimond pattern."""


try:
    row_size = int(input("Enter the size of rows: "))
    if row_size <= 1:
        raise ValueError("Size of rows must be greater than one.")
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for i in range(1, row_size + 1):
        print(" " * (row_size - i), end="")
        print(" * " * i)
    for i in range(row_size - 1, 0, -1):
        print(" " * (row_size - i), end="")
        print(" * " * i)
