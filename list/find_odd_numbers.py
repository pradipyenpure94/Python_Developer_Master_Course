"""Find the odd numbers."""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(f"Odd numbers: {odd_numbers}")
