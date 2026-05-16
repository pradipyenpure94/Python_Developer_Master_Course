"""Separate positive and negative numbers."""

numbers = [0, 1, 2, -3, 4, -5, 6, -1, 2, 3]

positive_numbers = []
negative_numbers = []

for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)

print(f"Positive numbers: {positive_numbers}\
      \nNegative numbers: {negative_numbers}")
