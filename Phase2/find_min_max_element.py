"""Find minimum and maximum element"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if numbers:
    min_number = numbers[0]
    max_number = numbers[0]

    for number in numbers[1:]:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number

    print(f"Minimum element: {min_number}")
    print(f"Maximum element: {max_number}")
else:
    print("List is empty!")
