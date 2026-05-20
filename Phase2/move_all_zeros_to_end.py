"""Move all zeros to end."""

numbers = [1, 2, 0, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 1, 4, 5]

if numbers:
    position = 0

    for number in numbers:
        if number != 0:
            numbers[position] = number
            position += 1

    while position < len(numbers):
        numbers[position] = 0
        position += 1

    print(f"Move all zeros to end: {numbers}")
else:
    print("List is empty!")
