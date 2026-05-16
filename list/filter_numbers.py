"""Separate positive and negative numbers."""

numbers = [0, 1, 2, -3, 4, -5, 6, -1, 2, 3]

positive_numbers = [x for x in numbers if x > 0]
negative_numbers = [x for x in numbers if x < 0]

print(f"Positive numbers: {positive_numbers}\
      \nNegative numbers: {negative_numbers}")
