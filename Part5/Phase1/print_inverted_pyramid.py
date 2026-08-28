"""Print an inverted pyramid."""


try:
    rows = int(input("Enter the size of rows: "))
    if rows <= 0:
        raise ValueError("Rows size must be greater than zero.")
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for i in range(rows, 0, -1):
        print(" " * (rows - i), end="")
        print(" * " * i)
