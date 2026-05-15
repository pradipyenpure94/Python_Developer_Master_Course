"""Linear search."""

numbers = [10, 20, 30, 40, 50, 60, 70]
search_number = 40

for index, number in enumerate(numbers):
    if search_number == number:
        print(f"Number found at index {index}")
        break
else:
    print("Number not found in list.")
