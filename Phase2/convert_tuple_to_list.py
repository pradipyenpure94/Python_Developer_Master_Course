"""Convert tuple to list."""

numbers = (2, 4, 6, 8, 10)

numbers_list = []
index = 0

while index < len(numbers):
    number = numbers[index]
    numbers_list.append(number)

    index += 1

print(f"Converted tuple to list: {numbers_list}")
