"""Reverse a list."""

numbers = [1, 2, 3, 4, 5]
n = len(numbers)
result = [numbers[index] for index in range(n - 1, -1, -1)]

print(f"Reversed List: {result}")
