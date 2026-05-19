"""Find minimum and maximum element"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if numbers:
    minimum_element = min(numbers)
    maximum_element = max(numbers)

    print(f"Minimum element: {minimum_element}")
    print(f"Maximum element: {maximum_element}")
else:
    print("List is empty!")
