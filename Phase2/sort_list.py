"""Sorted List"""

numbers = [10, 50, 40, 20, 30, 50, 80, 90, 70, 60, 40, 20]

for i in range(len(numbers)):
    swapped = False
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

    if not swapped:
        break

print(f"Sorted numbers: {numbers}")
