"""Find the largest and smallest numbers without max() or min()."""

numbers = [-1, -2, -3, -4, 0, 1, 2, 3, 4, 5, 7, 8, 9]

if not numbers:
    print("List is empty.")
else:
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number

    print(f"Smallest : {smallest}")
    print(f"Largest  : {largest}")
