"""Find missing numbers in list."""

numbers = [1, 3, 5, 7, 9, 10]
all_numbers = list(range(min(numbers), max(numbers) + 1))

missing_numbers = [number for number in all_numbers if number not in numbers]
print(f"Missing numbers: {missing_numbers}")
