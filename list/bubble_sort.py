"""Bubble sort using list."""

numbers = [10, 20, 30, 45, 63, 14, 18, 15, 12]

length = len(numbers)
i = 0
while i < length:
    swapped = False
    j = 0

    while j < length - i - 1:
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

        j += 1

    i += 1

    if not swapped:
        break

print(f"Sorted numbers: {numbers}")
