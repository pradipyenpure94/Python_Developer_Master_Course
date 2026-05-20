"""Bubble sort implementation."""

numbers = [10, 20, 50, 60, 40, 80, 70, 90]

numbers_count = len(numbers)

for i in range(numbers_count):
    swapped = False

    for j in range(0, numbers_count - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

    if not swapped:
        break

print(f"Sorted numbers: {numbers}")
