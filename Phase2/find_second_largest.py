"""Find second largest number from list."""

numbers = [102, 0, 30, 4, 0, 50, 607, 0, 80, 90, 100]

largest_number = second_largest_number = float('-inf')

for number in numbers:
    if number > largest_number:
        second_largest_number = largest_number
        largest_number = number
    elif number >= second_largest_number and number != largest_number:
        second_largest_number = number

if second_largest_number != float('-inf'):
    print(f"Second Largest number: {second_largest_number}")
else:
    print("Second largest number not found (May be equal numbers)")
