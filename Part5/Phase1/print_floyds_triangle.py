"""Print Floyds triangle."""

try:
    rows_size = int(input("Enter the size of rows: "))
    if rows_size <= 0:
        raise ValueError("Row size must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    current_num = 1
    for i in range(1, rows_size + 1):
        for _ in range(i):
            print(current_num, end=" ")
            current_num += 1
        print()
