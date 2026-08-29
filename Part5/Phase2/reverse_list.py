"""Reverse a list."""

numbers = [1, 2, 3, 4, 5]
n = len(numbers) - 1
result = []
index = 0

while n >= index:
    result.append(numbers[n])
    n -= 1

print(f"Reversed List: {result}")
