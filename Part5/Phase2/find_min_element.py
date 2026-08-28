"""Find minimum element."""


numbers = [1, 2, 0, 4, 6, 8]

min_number = numbers[0]

for number in numbers:
    if number < min_number:
        min_number = number

print(f"Minimum number: {min_number}")
