"""Print a pyramid pattern."""


try:
    rows = int(input("Enter the rows of pyramid: "))
    if rows <= 0:
        raise ValueError("Rows size must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print(" * " * i)
