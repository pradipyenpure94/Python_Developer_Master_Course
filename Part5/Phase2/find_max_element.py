"""Find maximum element."""


numbers = [1, 2, 3, 4, 5]
maximum_number = numbers[0]

for number in numbers:
    if maximum_number < number:
        maximum_number = number

print(f"Maximum element: {maximum_number}")
