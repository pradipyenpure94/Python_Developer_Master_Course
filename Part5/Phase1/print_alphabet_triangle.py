"""Print alphabet triangle."""


current_num = 65

try:
    row_size = int(input("Enter the size of row: "))
    if row_size <= 0:
        raise ValueError("Size row must be greater than zero.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    for i in range(1, row_size + 1):
        for _ in range(i):
            print(chr(current_num), end=" ")
            current_num += 1
        print()
