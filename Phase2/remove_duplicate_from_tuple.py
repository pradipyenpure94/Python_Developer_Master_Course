"""Remove duplicate from tuple."""

numbers = (1, 2, 3, 1, 5, 6, 2, 4, 5, 6, 7, 8, 9, 5)

seen = set()
unique_numbers = []
index = 0

while index < len(numbers):
    number = numbers[index]
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)
    index += 1

result = tuple(unique_numbers)
print(f"Unique numbers: {result}")
