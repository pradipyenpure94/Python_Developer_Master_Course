"""Sum of list elements."""

numbers = [1, 2, 3, 4, 5, 6]

total = 0
length = len(numbers)
i = 0

while i < length:
    total += numbers[i]
    i += 1

print(f"Sum of list elements: {total}")
