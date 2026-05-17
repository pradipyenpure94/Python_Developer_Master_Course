"""Frequency of each element."""

numbers = (1, 2, 3, 4, 5, 6, 2, 5, 9, 2, 4, 7, 1, 5, 9, 3, 5, 4)

unique_numbers = list(set(numbers))
index = 0

while index < len(unique_numbers):
    current_number = unique_numbers[index]

    print(current_number, "frequency of : ", numbers.count(current_number))
    index += 1
