"""Find index of element."""

numbers = (1, 2, 3, 1, 5, 6, 1, 4, 7, 18, 9)
target = 1
start = 4
end = 7

if target in numbers[start:end]:
    print(f"Index of {target} is : {numbers.index(target, start, end)}")
else:
    print("Element not found in given tuple range.")
