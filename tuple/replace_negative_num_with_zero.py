"""Replace negative numbers with zero."""

numbers = (-1, -2, 3, 4, 56, -9, -8, -7, 56, 23)

# Replace negative number with zero
updated_numbers = tuple(0 if number < 0 else number for number in numbers)
print(f"Negative numbers replaced with zero: {updated_numbers}")
