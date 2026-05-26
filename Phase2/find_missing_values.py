"""Find missing values using set difference."""

numbers = {1, 2, 3, 5, 7, 8, 9, 10}

full_numbers = set(range(1, 11))
missing_numbers = set()

for number in full_numbers:
    if number not in numbers:
        missing_numbers.add(number)

print(f"Missing numbers: {missing_numbers}")
