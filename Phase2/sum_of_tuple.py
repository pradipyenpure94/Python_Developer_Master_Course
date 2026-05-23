"""Find sum of tuple elements."""

numbers = (1, 2, 3, 4, 5, 6)

total = 0
index = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

print(f"Sum of numbers (tuple): {total}")
