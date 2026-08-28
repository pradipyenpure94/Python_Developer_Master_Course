"""Find maximum element."""


numbers = [1, 2, 3, 4, 5]
maximum_number = numbers[0]
index = 0

while index < len(numbers):
    if maximum_number < numbers[index]:
        maximum_number = numbers[index]
    index += 1
print(f"Maximum element: {maximum_number}")
