"""Frequency of each element."""

numbers = (1, 2, 3, 4, 5, 6, 2, 5, 9, 2, 4, 7, 1, 5, 9, 3, 5, 4)

for number in set(numbers):
    print(number, "frequency of : ", numbers.count(number))
