"""Find minimum and maximum value."""

numbers = [1, 4, 7, 8, 5, 2, 3, 6, 9]

if numbers:
    min_value = numbers[0]
    max_value = numbers[0]

    for number in numbers[1:]:
        if number < min_value:
            min_value = number
        elif number > max_value:
            max_value = number

    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
else:
    print("List is empty.")
