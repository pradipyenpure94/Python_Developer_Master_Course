"""Find second largest number from list."""

numbers = [102, 0, 30, 4, 0, 50, 607, 0, 80, 90, 100]

largest_number = second_largest_number = float('-inf')
index = 0
list_length = len(numbers)

while index < list_length:
    current_number = numbers[index]

    if current_number > largest_number:
        second_largest_number = largest_number
        largest_number = current_number
    elif current_number >= second_largest_number and \
        current_number != largest_number:
        second_largest_number = current_number

    index += 1

if second_largest_number != float('-inf'):
    print(f"Second Largest number: {second_largest_number}")
else:
    print("Second largest number not found (May be equal numbers)")
