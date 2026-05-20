"""Selection sort implementation."""

numbers = [10, 20, 50, 60, 40, 80, 70, 90]

numbers_count = len(numbers)

for i in range(numbers_count - 1):
    min_index = i
    for j in range(i + 1, numbers_count):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(f"Sorted numbers: {numbers}")
