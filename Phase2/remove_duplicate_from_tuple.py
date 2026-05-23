"""Remove duplicate from tuple."""

numbers = (1, 2, 3, 1, 5, 6, 2, 4, 5, 6, 7, 8, 9, 5)

unique_numbers = tuple(dict.fromkeys(numbers))
print(f"Unique numbers: {unique_numbers}")
