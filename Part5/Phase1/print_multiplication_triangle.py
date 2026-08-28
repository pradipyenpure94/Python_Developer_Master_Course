"""Print multiplication triangle."""


try:
    rows_size = int(input("Enter the size of rows: "))
    if rows_size <= 0:
        raise ValueError("Row size must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for row in range(1, rows_size + 1):
        for column in range(1, row + 1):
            print(row * column, end=" ")
        print()
