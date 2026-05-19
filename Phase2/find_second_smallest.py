"""Find the second smallest number from list."""

numbers = [40, 50, 60, 20, 30, 10, 80, 90, 70]

smallest = second_smallest = float('inf')

for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif smallest < number < second_smallest:
        second_smallest = number

if second_smallest != float('inf'):
    print(f"Second smallest number: {second_smallest}")
else:
    print("Second smallest number not found (Numbers may be equal)")
