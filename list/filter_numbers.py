"""Separate positive and negative numbers."""

numbers = [0, 1, 2, -3, 4, -5, 6, -1, 2, 3]

positive_numbers = []
negative_numbers = []
index = 0
length = len(numbers)

while index < length:
    current_number = numbers[index]
    if current_number > 0:
        positive_numbers.append(current_number)
    elif current_number < 0:
        negative_numbers.append(current_number)
    index += 1

print(f"Positive numbers: {positive_numbers}\
      \nNegative numbers: {negative_numbers}")
