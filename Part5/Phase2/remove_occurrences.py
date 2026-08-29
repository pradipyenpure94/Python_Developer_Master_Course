"""Remove all occurrences of a given element."""


numbers = [9, 7, 6, 4, 8, 3, 7, 9, 3, 9]
target = 9

numbers = [num for num in numbers if num != target]

print(f"After remove all occurrences of {target}: {numbers}")
