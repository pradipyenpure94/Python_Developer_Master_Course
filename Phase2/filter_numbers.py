"""Separate positive and negative numbers."""

numbers = [-1, -2, 5, 6, 4, -9, -8, 4, 2, 3, -9]

positive_numbers = []
negative_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)
    elif number < 0:
        negative_numbers.append(number)

print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")
