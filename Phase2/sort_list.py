"""Sorted List"""

numbers = [10, 50, 40, 20, 30, 50, 80, 90, 70, 60, 40, 20]

i = 0
list_length = len(numbers)

while i < list_length:
    swapped = False

    j = 0

    while j < (list_length - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

        j += 1

    if not swapped:
        break

    i += 1

print(f"Sorted numbers: {numbers}")
