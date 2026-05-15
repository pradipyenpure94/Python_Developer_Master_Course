"""Find the smallest number."""

numbers = [10, 50, 20, 90, 40]

if numbers:
    smallest_number = numbers[0]

    for number in numbers[1:]:
        if number < smallest_number:
            smallest_number = number

    print(f"Smallest number: {smallest_number}")
else:
    print("List is empty!")
