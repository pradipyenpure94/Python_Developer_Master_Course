"""Find second largest element."""


numbers = [1, 9, 9, 3]

first_largest = second_largest = float('-inf')

if len(set(numbers)) < 2:
    print("A second distinct largest element does not exist.")
else:
    for number in numbers:
        if number > first_largest:
            second_largest = first_largest
            first_largest = number
        elif number > second_largest and first_largest != number:
            second_largest = number

    print(f"Second Largest Element: {second_largest}")
