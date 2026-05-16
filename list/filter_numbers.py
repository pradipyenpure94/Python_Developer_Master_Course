"""Separate positive and negative numbers."""

numbers = [0, 1, 2, -3, 4, -5, 6, -1, 2, 3]

positive_numbers = list(filter(lambda x: x > 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))

print(f"Positive numbers: {positive_numbers}\
      \nNegative numbers: {negative_numbers}")
