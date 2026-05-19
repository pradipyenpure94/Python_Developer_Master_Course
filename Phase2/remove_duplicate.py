"""Remove duplicates element from list."""

numbers = [10, 50, 40, 20, 30, 50, 80, 90, 70, 60, 40, 20]

unique_numbers = list(dict.fromkeys(numbers))
print(f"Unique numbers: {unique_numbers}")
