"""Find the second largest number in tuple."""

t = (1, 2, 3, 4, 5, 6)

if len(t) < 2:
    print("Tuple must contain at least two elements.")
else:
    first_number = second_number = float('-inf')

    for number in t:
        if number > first_number:
            second_number = first_number
            first_number = number
        elif number >= second_number and number != first_number:
            second_number = number
    if second_number == float('-inf'):
        print("No second largest number found (may be equal number).")
    else:
        print(f"Second largest number: {second_number}")
