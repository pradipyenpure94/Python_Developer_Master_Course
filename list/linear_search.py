"""Linear search."""

numbers = [10, 20, 30, 40, 50, 60, 70]

search_number = 40
index = 0
length = len(numbers)

while index < length:
    if search_number == numbers[index]:
        print(f"Number found at index {index}")
        break
    index += 1
else:
    print("Number not found in list.")
