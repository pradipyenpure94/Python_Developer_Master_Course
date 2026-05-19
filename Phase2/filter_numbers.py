"""Separate positive and negative numbers from list."""

numbers = [-1, -2, 5, 6, 4, -9, -8, 4, 2, 3, -9]

positive_numbers = []
negative_numbers = []
index = 0
list_length = len(numbers)


while index < list_length:
    current_number = numbers[index]
    if current_number > 0:
        positive_numbers.append(current_number)
    elif current_number < 0:
        negative_numbers.append(current_number)

    index += 1

print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")
