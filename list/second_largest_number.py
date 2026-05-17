"""Second largest number."""

numbers = [10, 50, 90, 60, 70, 40]

if len(numbers) < 2:
    print("Second largest does not exist!")
else:
    first = second = float('-inf')
    index = 0
    length = len(numbers)

    while index < length:
        current_number = numbers[index]
        if current_number > first:
            second = first
            first = current_number
        elif current_number >= second and current_number != first:
            second = current_number
        index += 1

    if second == float('-inf'):
        print("No second largest element found (all elements may be equal)")
    else:
        print(f"Second Largest: {second}")
