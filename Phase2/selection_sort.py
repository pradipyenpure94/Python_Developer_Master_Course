"""Selection sort implementation."""

numbers = [10, 20, 50, 60, 40, 80, 70, 90]

numbers_count = len(numbers)

i = 0

while i < numbers_count - 1:
    min_index = i
    j = i + 1

    while j < numbers_count:
        if numbers[j] < numbers[min_index]:
            min_index = j

        j += 1

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    i += 1

print(f"Sorted numbers: {numbers}")
