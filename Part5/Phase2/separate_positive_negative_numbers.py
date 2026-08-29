"""Separate positive and negative numbers."""

numbers = [-1, -2, -3, 4, 5, -6, 8, 9, 0]

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]
print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")
