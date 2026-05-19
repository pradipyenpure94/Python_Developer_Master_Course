"""Find minimum and maximum element"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if numbers:
    min_number = numbers[0]
    max_number = numbers[0]
    index = 1

    while index < len(numbers):
        current_number = numbers[index]
        if current_number < min_number:
            min_number = current_number
        elif current_number > max_number:
            max_number = current_number
        index += 1

    print(f"Minimum element: {min_number}")
    print(f"Maximum element: {max_number}")
else:
    print("List is empty!")
