"""Find missing values using set difference."""

numbers = {1, 2, 3, 5, 7, 8, 9, 10}

full_numbers = list(range(1, 11))
missing_numbers = set()
index = 0

while index < len(full_numbers):
    number = full_numbers[index]
    if number not in numbers:
        missing_numbers.add(number)
    index += 1

print(f"Missing numbers: {missing_numbers}")
