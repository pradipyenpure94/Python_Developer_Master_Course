"""Find the smallest number."""

numbers = [10, 50, 20, 90, 40]

if numbers:
    smallest_number = numbers[0]
    i = 1
    length = len(numbers)

    while i < length:
        if numbers[i] < smallest_number:
            smallest_number = numbers[i]
        i += 1

    print(f"Smallest number: {smallest_number}")
else:
    print("List is empty!")
