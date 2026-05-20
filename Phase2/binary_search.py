"""Binary search using list."""

numbers = [10, 20, 50, 60, 40, 80, 70, 90]
target = 90

numbers = sorted(numbers)
print(f"Numbers: {numbers}")
left = 0
right = len(numbers) - 1
found = False
index = -1

while left <= right:
    index = (left + right) // 2

    if numbers[index] == target:
        found = True
        break
    elif numbers[index] < target:
        left = index + 1
    else:
        right = index - 1

if found:
    print(f"Index of {target} is {index}")
else:
    print(f"{target} number is not found in list: {numbers}.")
