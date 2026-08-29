"""Find the least frequent of element."""

numbers = [9, 7, 6, 4, 8, 3, 7, 9, 3, 9]

frequency_of_numbers = {}

for number in numbers:
    frequency_of_numbers[number] = frequency_of_numbers.get(number, 0) + 1

print(f"Frequency of numbers: {frequency_of_numbers}")

least_frequent = min(frequency_of_numbers, key=frequency_of_numbers.get)
print(f"Least frequenct element: {least_frequent}")
