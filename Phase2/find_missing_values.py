"""Find missing values using set difference."""

numbers = {1, 2, 3, 5, 7, 8, 9, 10}
full_numbers = set(range(1, 11))

missing_numbers = full_numbers.difference(numbers)
print(f"Missing numbers: {missing_numbers}")
