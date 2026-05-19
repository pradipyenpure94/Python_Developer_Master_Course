"""Reverse a list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reversed_numbers = []
index = len(numbers) - 1

while index >= 0:
    reversed_numbers.append(numbers[index])
    index -= 1

print(f"Reversed List: {reversed_numbers}")
