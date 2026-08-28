"""Print a number triangle."""


try:
    row_size = int(input("Enter the size of rows: "))
    if row_size <= 0:
        raise ValueError("Row size must be greater zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for i in range(1, row_size + 1):
        for _ in range(i):
            print(i, end=" ")
        print()
