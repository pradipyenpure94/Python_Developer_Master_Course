"""Find the frequency of every element."""

numbers = [9, 7, 6, 4, 8, 3, 7, 9, 3, 9]

frequency_of_numbers = {}

for number in numbers:
    frequency_of_numbers[number] = frequency_of_numbers.get(number, 0) + 1

print(f"Frequency of numbers: {frequency_of_numbers}")
