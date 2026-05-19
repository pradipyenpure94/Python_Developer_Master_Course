"""Separate positive and negative numbers."""

numbers = [-1, -2, 5, 6, 4, -9, -8, 4, 2, 3, -9]

positive_numbers = list(filter(lambda number: number > 0, numbers))
negative_numbers = list(filter(lambda number: number < 0, numbers))
print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")
