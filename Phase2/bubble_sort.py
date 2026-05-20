"""Bubble sort implementation."""

numbers = [10, 20, 50, 60, 40, 80, 70, 90]

numbers_count = len(numbers)

i = 0
while i < numbers_count - 1:
    swapped = False
    j = 0

    while j < numbers_count - i - 1:
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

        j += 1

    if not swapped:
        break

    i += 1

print(f"Sorted numbers: {numbers}")
