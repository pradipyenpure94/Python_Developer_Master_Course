"""Binary search."""

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
search_number = 40

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2
    if search_number == numbers[mid]:
        print(f"Number found at index {mid}")
        break
    elif numbers[mid] < search_number:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Number not found in list.")
