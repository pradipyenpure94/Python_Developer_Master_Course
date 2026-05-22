"""Find minimum and maximum value."""

numbers = [1, 4, 7, 8, 5, 2, 3, 6, 9]

if numbers:
    min_value = numbers[0]
    max_value = numbers[0]
    index = 1

    while index < len(numbers):
        current_number = numbers[index]
        if current_number < min_value:
            min_value = current_number
        elif current_number > max_value:
            max_value = current_number

        index += 1

    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
else:
    print("List is empty.")
