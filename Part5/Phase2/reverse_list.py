"""Reverse a list."""

numbers = [1, 2, 3, 4, 5]
n = len(numbers)
result = []

for index in range(n - 1, -1, -1):
    result.append(numbers[index])

print(f"Reversed List: {result}")
