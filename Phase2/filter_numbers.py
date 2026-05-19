"""Separate positive and negative numbers."""

numbers = [-1, -2, 5, 6, 4, -9, -8, 4, 2, 3, -9]

positive_numbers = [number for number in numbers if number > 0]
negative_numbers = [number for number in numbers if number < 0]
print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")
