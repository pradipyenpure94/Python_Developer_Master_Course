"""Convert list to tuple."""

numbers = [2, 4, 6, 8, 10]

numbers_tuple = ()

for number in numbers:
    numbers_tuple += (number,)

print(f"Converted list to tuple: {numbers_tuple}")
