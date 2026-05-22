"""Count occurrences of element."""

numbers = (1, 2, 3, 4, 5, 6, 1, 5, 9, 7, 8, 9, 1)
target = 1

count = 0
index = 0

while index < len(numbers):
    number = numbers[index]
    if number == target:
        count += 1

    index += 1

print(f"{target} appeared {count} times.")
