"""Find indexes of all occurrences in tuple."""

numbers = (1, 2, 3, 2, 5, 8, 2, 6, 9)

target_number = 2

for index, value in enumerate(numbers):
    if value == target_number:
        print(f"Found {target_number} at index {index}")
