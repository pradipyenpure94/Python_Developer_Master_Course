"""Swap first and last element"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if numbers:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    print(f"After swapping elements: {numbers}")
else:
    print("No elements found in list.")
