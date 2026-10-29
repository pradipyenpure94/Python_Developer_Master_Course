"""Find the second-largest distinct number in a list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(set(numbers)) < 2:
    print("No second largest number found.")
else:
    largest = second_largest = float("-inf")

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    print(f"Second Largest number: {second_largest}")
