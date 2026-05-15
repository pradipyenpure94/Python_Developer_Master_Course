"""Find the largest number."""


numbers = [10, 50, 20, 90, 40]

if numbers:
    largest_number = numbers[0]
    i = 1
    length = len(numbers)

    while i < length:
        if numbers[i] > largest_number:
            largest_number = numbers[i]
        i += 1

    print(f"Largest number: {largest_number}")
else:
    print("List is empty!")
