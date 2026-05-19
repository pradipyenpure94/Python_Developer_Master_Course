"""Reverse a list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reversed_numbers = []
for index in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[index])

print(f"Reversed List: {reversed_numbers}")
