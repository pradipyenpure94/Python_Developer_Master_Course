"""Convert list to tuple."""

numbers = [2, 4, 6, 8, 10]

numbers_tuple = ()
index = 0

while index < len(numbers):
    number = numbers[index]
    numbers_tuple += (number, )
    index += 1

print(f"Converted list to tuple: {numbers_tuple}")
