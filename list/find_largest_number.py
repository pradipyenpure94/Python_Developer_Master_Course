"""Find the largest number."""


numbers = [10, 50, 20, 90, 40]

if numbers:
    largest_number = numbers[0]

    for number in numbers[1:]:
        if number > largest_number:
            largest_number = number

    print(f"Largest number: {largest_number}")
else:
    print("List is empty!")
