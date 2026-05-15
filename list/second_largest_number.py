"""Second largest number."""

numbers = [10, 50, 90, 60, 70, 40]

if len(numbers) < 2:
    print("Second largest does not exist!")
else:
    first = second = float('-inf')

    for number in numbers:
        if number > first:
            second = first
            first = number
        elif number > second and number != first:
            second = number

    if second == float('-inf'):
        print("No second largest element found (all elements may be equal)")
    elif second != float('-inf'):
        print(f"Second Largest: {second}")
