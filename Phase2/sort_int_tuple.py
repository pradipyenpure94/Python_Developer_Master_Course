"""Sort integer tuple."""

numbers = (10, 2, 8, 5)

# Bubble sort algorithm
numbers_list = list(numbers)

for i in range(len(numbers_list)):
    swapped = False
    for j in range(len(numbers_list) - i - 1):
        if numbers_list[j] > numbers_list[j + 1]:
            numbers_list[j], numbers_list[j + 1] = (numbers_list[j + 1],
                                                    numbers_list[j])
            swapped = True
    if not swapped:
        break

sorted_tuple = tuple(numbers_list)
print(f"Sorted tuple: {sorted_tuple}")
