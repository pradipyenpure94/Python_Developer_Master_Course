"""Find repeated items in tuple."""

numbers = (1, 2, 3, 1, 5, 9, 2, 5, 8, 3, 4, 7, 2, 5, 9, 8, 5, 4, 2, 1)

repeated_items = []

for index, number in enumerate(numbers):
    if (numbers.count(number) > 1 and number not in numbers[:index]):
        repeated_items.append(number)

print(f"Repeated items: {repeated_items}")
