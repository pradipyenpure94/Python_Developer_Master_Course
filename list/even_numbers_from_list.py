"""Even numbers from list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
length = len(numbers)

while i < length:
    if numbers[i] % 2 == 0:
        print(numbers[i])
    i += 1
