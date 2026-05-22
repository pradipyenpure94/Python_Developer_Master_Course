"""Find index of element."""

numbers = (1, 2, 3, 1, 5, 6, 1, 4, 7, 18, 9)
target = 1
start = 4
end = 7

while start < end:
    number = numbers[start]
    if number == target:
        print(f"Index of {target} is {start}")
        break
    start += 1

else:
    print("Element not found in given tuple range.")
