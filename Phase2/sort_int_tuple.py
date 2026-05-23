"""Sort integer tuple."""

numbers = (10, 2, 8, 5)

# Selection sort algorithm
numbers_list = list(numbers)

for i, _ in enumerate(numbers_list):
    min_index = i

    for j in range(i + 1, len(numbers_list)):
        if numbers_list[j] < numbers_list[min_index]:
            min_index = j

    # Swap only if needed
    if i != min_index:
        numbers_list[i], numbers_list[min_index] = (numbers_list[min_index],
                                                    numbers_list[i])

# Convert back to tuple
sorted_tuple = tuple(numbers_list)
print(f"Sorted tuple: {sorted_tuple}")
