"""Find second smallest element."""

numbers = [1, 9, 9, 3]
first_smallest = second_smallest = float('inf')

if len(set(numbers)) < 2:
    print("A second distinct smallest element does not exist.")
else:
    for number in numbers:
        if number < first_smallest:
            second_smallest = first_smallest
            first_smallest = number
        elif number < second_smallest and number != first_smallest:
            second_smallest = number
    print(f"Second Smallest: {second_smallest}")
