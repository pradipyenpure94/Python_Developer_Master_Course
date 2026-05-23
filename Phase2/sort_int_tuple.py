"""Sort integer tuple."""

numbers = (10, 2, 8, 5)

# Insertion sort algorithm
numbers_list = list(numbers)

for i, _ in enumerate(numbers_list):
    current = numbers_list[i]
    j = i - 1

    while j >= 0 and numbers_list[j] > current:
        numbers_list[j + 1] = numbers_list[j]
        j -= 1

    numbers_list[j + 1] = current

# Convert back to tuple
sorted_tuple = tuple(numbers_list)
print(f"Sorted tuple: {sorted_tuple}")
