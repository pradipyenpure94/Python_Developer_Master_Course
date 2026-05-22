"""Count occurrences of element."""

numbers = (1, 2, 3, 4, 5, 6, 1, 5, 9, 7, 8, 9, 1)
target = 1

count = sum(number == target for number in numbers)
print(f"{target} appeared {count} times.")
