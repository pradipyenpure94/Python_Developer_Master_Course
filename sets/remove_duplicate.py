"""Remove duplicates from list."""

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(dict.fromkeys(numbers))
print(f"Unique numbers: {unique_numbers}")
