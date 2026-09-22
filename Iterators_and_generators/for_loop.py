"""Compare for loop with manual iterator."""


even_numbers = [2, 4, 6, 8, 10]

iterator = iter(even_numbers)

for number in iterator:
    print(number)
