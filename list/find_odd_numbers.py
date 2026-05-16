"""Find the odd numbers."""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 == 1]
print(f"Odd numbers: {odd_numbers}")
